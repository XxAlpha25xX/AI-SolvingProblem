<template>
  <div id="container-global-queen">
    <ul id="container-queen">
      <div v-for="line in tile" class="line-puzzle">
        <div v-for="i in line">
          <li v-if="i == 0" class="empty tile"></li>
          <li v-else class="tile"></li>
        </div>
      </div>
    </ul>
  </div>
</template>

<script lang="ts">
import {
  Component,
  //  Inject,
  //  Model,
  Prop,
  //  Provide,
  Watch,
  Vue
} from 'nuxt-property-decorator'

@Component
export default class Puzzle extends Vue {

  @Prop({ default: []})
    tile!: []

  trueSize: number = 0
  sqrtTrueSize: number = 0
  maxArea: number = 600

  mounted () {
    window.addEventListener('DOMContentLoaded', () => {
      this.changedTile()
    })
  }

  isGood() {
    return (this.sqrtTrueSize * this.sqrtTrueSize === this.trueSize)
  }

  @Watch('tile')
  changedTile () {
    let containerGlobal = <HTMLElement>document.getElementById('container-queen')

    this.resetValue()
    //console.log(this.tile)
    if (containerGlobal) {
      if (!this.isGood()) {
        containerGlobal.style.display = 'none'
        return
      } else {
        containerGlobal.style.display = 'grid'
      }
      containerGlobal.style.gridTemplateColumns = `1fr`
      containerGlobal.style.gridTemplateRows = `repeat(${this.sqrtTrueSize}, 1fr)`

      this.updateLine(0.001)
      this.updateLine(0.002)
      this.updateLine(0.005)
      this.updateLine(0.01)
      this.updateLine(0.05)
    }
  }

  updateLine (nb: number) {
    setTimeout(async () => {
        let linePuzzle = <HTMLCollection>document.getElementsByClassName('line-puzzle')

        if (linePuzzle) {
          Array.from(linePuzzle).forEach((element, index, array) => {
            let e = <HTMLElement>element
            if (this.sqrtTrueSize >= 10) {
              e.style.fontSize = `1rem`
            } else {
              e.style.fontSize = `2rem`
            }
            e.style.gridTemplateColumns = `repeat(${this.sqrtTrueSize}, 1fr)`
          })
        }
      }, 1000 * nb)
  }

  resetValue () {
    this.trueSize = this.tile.length * this.tile.length
    this.sqrtTrueSize = this.tile.length
  }
}
</script>

<style lang="scss" scoped>
  #container-global-queen {
    width: 620px;
    height: 620px;
    background: white;
    border-radius: 10px;
    margin: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 33px 29px 15px -3px rgba(0,0,0,0.1);

    ul {
      width: 600px;
      height: 600px;
      display: grid;
      grid-column-gap: 10px;
      grid-row-gap: 10px;
      color: #E4FDE1;

      .empty {
        background: white;
        border: 2px solid #6300ff;
      }
    }
  }

  .tile {
    background: #6300ff;;
    border-radius: 7px;
    border: 1px solid #6300ff;
    text-align: center;
    display: flex;
    height: 100%;
    color: white;
    justify-content: center;
    align-items: center;
  }

  .line-puzzle {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    column-gap: 10px;
    font-size: 2rem;
  }

</style>
