<template>
  <div class="global">
    <div class="stuff">
      <p>Hello</p>
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

@Component
export default class Index extends Vue {
  name = 'Stuff'
}
</script>

<style lang="scss" scoped>
  .global {
    display: flex;
    background: blue;
    justify-content: center;
    height: 100vh;
    align-items: center;
    .stuff {
      width: 50px;
      height: 50px;
      background: red;
    }
  }
</style>
