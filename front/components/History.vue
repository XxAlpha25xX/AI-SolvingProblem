<template>
  <div class="container">
    <div v-if="history.length > 0" class="mb">
      <div v-for="h in (history.length - 1)" :key="h" class="case-container">
        <div v-if="h == i" class="case green" @click="onClickHistory(h)">
          <p>Move - {{ h }}</p>
          <div class="score">
            {{ score[h] }}
          </div>
        </div>
        <div v-else class="case" @click="onClickHistory(h)">
          <p>Move - {{ h }}</p>
          <div class="score">
            {{ score[h] }}
          </div>
        </div>
      </div>
    </div>
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
export default class history extends Vue {
  @Prop({ default: () => { return [] } })
    history!: []

  @Prop({ default: () => { return [] } })
    score!: []

  @Prop({ default: 0 })
    i!: number

  mounted () {
    window.addEventListener('DOMContentLoaded', () => {

    })
  }

  @Watch('history')
  addOneCaseToHistory () {
  }

  onClickHistory (i:number) {
    this.$emit('onClickHistory', i)
  }
}
</script>

<style lang="scss" scoped>
.mb {
  margin-bottom: 20px;
}
  .container {
    display: flex;flex-direction: column;
    width: 620px;
    height: 620px;
    background: white;
    margin: 10px;
    align-items: center;
    overflow-y: scroll;
    border-radius: 10px;
    box-shadow: 33px 29px 15px -3px rgba(0,0,0,0.1);

    div {
      width: 100%;
    }

    .case-container {
      width: 100%;
      display: flex;
      align-items: center;
      flex-direction: row;
      justify-content: center;

      .case {
        background: white;
        display: flex;
        flex-direction: row;
        color: gray;
        border-radius: 3px;
        background: white;
        width: 90%;
        margin: 15px 20px;
        font-size:35px;
        padding: 10px;
        transition: 0.2s all;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;

        p {
          height: fit-content;
        }

        .score {
          color: #6300ff;
          width: fit-content;
          height: 50px;
          width: 50px;
          overflow: hidden;
          padding : 5px;
          position: relative;
          display: flex;
          border-color: #6300ff;
          border-radius: 3px;
          border-style: solid;
          border-width: 3px;
          background: white;
          justify-content: center;
        }

        &:hover {
          background: #536bf57f;
          color: white;
          transform: scale(0.98);
        }

        &:active {
          transform: scale(0.95);
          background: rgb(0, 90, 192);
        }
      }
    }
  }

  .green {
    background: #3d009e !important;
    color: white !important;

    .score {
      color: rgb(9, 165, 22) !important;
      border-color: rgb(9, 165, 22) !important;

    }
  }

</style>
