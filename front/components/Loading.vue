<template>
  <div class="loader"></div>
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
export default class Loading extends Vue {

}
</script>

<style lang="scss" scoped>
  .loader {
    border: 16px solid #f3f3f3;
    border-radius: 50%;
    border-top: 16px solid #6300ff;
    width: 120px !important;
    height: 120px !important;
    -webkit-animation: spin 2s linear infinite;
    animation: spin 2s linear infinite;
  }


@-webkit-keyframes spin {
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

</style>
