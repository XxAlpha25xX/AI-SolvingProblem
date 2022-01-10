<template>
  <div class="global">
    <div class="top-buttons">
      <DropDown
        class="drop-down"
        :arr="algorithmList"
        type="algo"
        title="Algorithm"
        :picked="settings.algo"
        @pick="pick"
      />
      <DropDown
        class="drop-down"
        :arr="problemList"
        title="Problem"
        :picked="settings.problem"
        type="problem"
        @pick="pick"
      />
      <DropDown
        class="drop-down"
        :arr="modeList"
        title="Mode"
        :picked="settings.mode"
        type="mode"
        @pick="pick"
      />
      <Input type="Size" placeholder="Number " @updateValueInput="updateValueInput" />
      <Input type="MaxMove" placeholder="Number " @updateValueInput="updateValueInput" />
      <Input type="Shuffle" placeholder="Number " @updateValueInput="updateValueInput" />
    </div>
    <div class="buttons">
      <Button type="paramButton" text="Go !" @onButtonClick="onButtonClick" />
    </div>
    <div v-if="loading" class="loader">
      <Loading />
    </div>
    <div v-if="error" class="loader" >
      <Error :text="errorText" />
    </div>
    <div class="child-components">
      <Puzzle v-if="settings.problem == 'NPuzzle'" :tile="currentState" />
      <Queen v-if="settings.problem == 'NQueen'" :tile="currentState" />
      <History :history="history" :score="score" :i="iState" @onClickHistory="onClickHistory" />
    </div>
    <div class="play-buttons">
      <Button type="resetButton" text="⏮" @onButtonClick="onButtonClick" />
      <Button type="playButton" text="▶️" @onButtonClick="onButtonClick" />
      <Button type="pauseButton" text="⏸" @onButtonClick="onButtonClick" />
      <Button type="solutionButton" text="🏁" @onButtonClick="onButtonClick" />
    </div>
  </div>
</template>

<script lang="ts">
import {
  Component,
  //  Inject,
  //  Model,
  //  Prop,
  //  Provide,
  //  Watch,
  Vue
} from 'nuxt-property-decorator'

interface Settings {
  algo?: string,
  problem?: string,
  mode?: string,
  size: number,
  maxMove: number,
  shuffle: number
}

@Component
export default class Solve extends Vue {
  algorithmList = ['HillClimbing', 'BreadthFirstSearch', 'A*']
  problemList = ['NPuzzle', 'NQueen']
  modeList = ['Tree', 'Graph']
  settings : Settings = { algo: '', problem: '', mode: '', size: 0, maxMove: 0, shuffle: 0 }
  transcriptAlgo = (_:any): string| undefined => { return '' }
  transcriptProblem = (_:any): string| undefined => { return '' }
  transcriptMode = (_:any): string| undefined => { return '' }
  currentState: number[][] = []
  history: number[][][] = []
  score :number[] = []
  game = {}
  tree = {}
  loading = false
  iState = 0
  pause = false
  error = false
  errorText = ''

  // http://localhost:9010/solve?nPuzzle=24&shuffle=7&problem=puzzle&algorithm=HillClimbing&mode=graph&maxMove=56
  async fetchData () {
    this.loading = true
    const res = await fetch(`http://localhost:9010/solve?size=${this.settings.size}&shuffle=${this.settings.shuffle}&problem=${this.settings.problem}&algorithm=${this.settings.algo}&mode=${this.settings.mode}&maxMove=${this.settings.maxMove}`)

    res.json().then((tmp) => {
      if (tmp.Ok) {
        this.loading = false
        console.log(tmp)
        this.iState = 1
        this.pause = true
        this.game = tmp
        this.history = tmp.stuff.history
        this.tree = tmp.stuff.tree
        this.score = tmp.stuff.score
        this.score.unshift(42)
        if (this.settings.algo === 'HillClimbing') {
          this.score.unshift(this.score[0] + 1)
        }
        this.history.unshift([])
        this.currentState = this.history[1]
      } else {
        this.loading = false
        this.error = true
        this.errorText = tmp.message
      }
    }).catch((err) => {
      this.loading = false
      this.error = true
      this.errorText = err
      console.log(err)
    })
  }

  pick (value: string, type: string) {
    if (type === 'algo') {
      this.settings.algo = this.transcriptAlgo(value)
    } else if (type === 'problem') {
      this.settings.problem = this.transcriptProblem(value)
    } else if (type === 'mode') {
      this.settings.mode = this.transcriptMode(value)
    }
  }

  updateValueInput (val: number, type: string) {
    if (type === 'Size') {
      if (val === 0 || isNaN(val)) {
        this.settings.size = 1
        return
      }
      this.settings.size = val
    } else if (type === 'MaxMove') {
      this.settings.maxMove = val
    } else if (type === 'Shuffle') {
      this.settings.shuffle = val
    }
  }

  onButtonClick (type: string) {
    this.error = false
    if (type === 'paramButton') {
      if (this.settings.problem === 'NQueen' && (this.settings.algo !== 'HillClimbing')) {
        this.error = true
        this.errorText = '🤷[Error] - Not implemented yet !'
      } else {
        this.error = false
        if (this.settings.shuffle === 0) {
          this.settings.shuffle = 1
        }
        this.fetchData()
      }
    } else if (type === 'resetButton') {
      this.iState = 1
      this.currentState = this.history[this.iState]
    } else if (type === 'pauseButton') {
      this.pause = true
    } else if (type === 'playButton') {
      this.pause = false
    } else if (type === 'solutionButton') {
      //this.pause = true
      this.iState = this.history.length - 1
      this.currentState = this.history[this.iState]
    }
  }

  playState () {
    setInterval(async () => {
      if (!this.pause) {
        this.iState += 1
        this.currentState = this.history[this.iState]

        if (this.iState > this.history.length - 1) {
          this.pause = true
          this.iState = this.history.length - 1
          this.currentState = this.history[this.iState]
        }
      }
    }, 1 * 1000)
  }

  onClickHistory (i: number) {
    this.currentState = this.history[i]
    this.iState = i
  }

  // Just wanted to try new stuff
  initTranscript () {
    this.transcriptAlgo = (algo: string) => ({
      HillClimbing: 'HillClimbing',
      BreadthFirstSearch: 'BreadthFirstSearch',
      'A*': 'A*'
    })[algo]
    this.transcriptProblem = (pb: string) => ({
      NPuzzle: 'NPuzzle',
      NQueen: 'NQueen'
    })[pb]
    this.transcriptMode = (mode: string) => ({
      Tree: 'Tree',
      Graph: 'Graph'
    })[mode]
  }

  initSettings () {
    this.settings.algo = this.algorithmList[0]
    this.settings.problem = this.problemList[0]
    this.settings.mode = this.modeList[0]
    this.settings.size = 8
    this.settings.maxMove = 64
    this.settings.shuffle = 0
  }

  mounted () {
    this.playState()
    this.initTranscript()
    this.initSettings()
  }
}
</script>

<style lang="scss" scoped>

  .global {
    background: #F8F8F8;
  }
  .top-buttons {
    margin-top: 20px;
    flex-grow: 1;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    flex-wrap: wrap;

    .drop-down {
      flex-basis: 33%;
      display: flex;
      justify-content: center;
    }
  }

  .buttons {
    display: flex;
    margin-top: 40px;
    justify-content: center;
    align-items: center;
  }

  .child-components {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .loader {
    display: flex;
    margin-top: 30px;
    margin-bottom: 30px;
    justify-content: center;
    height: fit-content;
    align-items: center;
  }
  .play-buttons {
    width: 15%;
    margin-left : auto;
    margin-right: auto;
    display: flex;
    margin-top: 30px;
    margin-bottom: 30px;
    justify-content: space-around;
    height: fit-content;
    align-items: center;
  }
</style>
