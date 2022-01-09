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
  algo: string,
  problem: string,
  mode: string,
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
  transcriptAlgo = (a:any) => {}
  transcriptProblem = (a:any) => {}
  transcriptMode = (a:any) => {}
  transcriptAPM = (a:any, b: any) => {}
  binderAPM = (a:any, b: any) => {}

  async fetchData () {
    const res = await fetch('http://localhost:9010/solve?')

    res.json().then((tmp) => {

    }).catch((err) => {
      console.log(err)
    })
  }

  pick (value: string, type: string) {
    this.transcriptAPM(value, type)(value)
  }

  updateValueInput (val: number, type: string) {
    if (type === 'Size') {
      this.settings.size = val
    } else if (type === 'MaxMove') {
      this.settings.maxMove = val
    } else if (type === 'Shuffle') {
      this.settings.shuffle = val
    }
    console.log(this.settings)
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
    this.transcriptAPM = (value: string, type : string) => ({
      algo: (value: string) => { this.settings.algo = this.transcriptAlgo(value) },
      problem: (value: string) => { this.settings.problem = this.transcriptProblem(value) },
      mode: (value: string) => { this.settings.mode = this.transcriptMode(value) }
    })[type]
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
    this.initTranscript()
    this.initSettings()
  }
}
</script>

<style lang="scss" scoped>
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
</style>
