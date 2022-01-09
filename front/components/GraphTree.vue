<template>
  <div class="global">
    <div id="canvas">

    </div>
  </div>
</template>

<script lang="ts" type="module">
import {
  Component,
  //  Inject,
  //  Model,
  Prop,
  //  Provide,
  Watch,
  Vue
} from 'nuxt-property-decorator'

import * as d3 from 'd3'

@Component
export default class GraphTree extends Vue {
  @Prop({ default: '' })
    type!: ''

  @Prop({ default: () => { return {} } })
    data!: {}

  @Watch('data')
  tree () {
  }

  mounted () {
    window.addEventListener('DOMContentLoaded', () => {
      this.tree()
    })
  }
}
</script>

<style lang="scss" scoped>
  .container {
    display: flex;flex-direction: column;
    width: 520px;
    height: 520px;
    background: #6300ff;
    margin: 10px;
    align-items: center;
    overflow-y: scroll;
    border-radius: 10px;
    }

</style>
