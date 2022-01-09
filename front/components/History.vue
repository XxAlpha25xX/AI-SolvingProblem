<template>
  <div class="container">
    <div v-if="history.length > 0" class="mb">
      <div v-for="h in (history.length - 1)" :key="h" class="case-container">
        <div class="case" @click="onClickHistory(h)">
          Move - {{ h }} - { {{ score[h] }} }
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
  @Prop({ default: [] })
    history!: []

  @Prop({ default: [] })
    score!: []

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
      justify-content: center;

      .case {
        background: white;
        border-radius: 3px;
        color: #6300ff;
        width: 90%;
        margin: 15px 0px;
        font-size:35px;
        padding: 10px;
        transition: 0.2s all;
        cursor: pointer;

        &:hover {
          background: #3d009e;
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

</style>
