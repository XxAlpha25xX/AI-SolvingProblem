<template>
  <div class="error">
    {{ text }}
  </div>
</template>

<script lang="ts">
import {
  Component,
  //  Inject,
  //  Model,
  Prop,
  //  Provide,
  // Watch,
  Vue
} from 'nuxt-property-decorator'

@Component
export default class Error extends Vue {
  @Prop({ default: '' })
    text!: string

  mounted () {
    window.addEventListener('DOMContentLoaded', () => {

    })
  }
}
</script>

<style lang="scss" scoped>

.error {
 background: rgb(255, 0, 106);
 width: 80%;
 text-align: center;
 padding: 15px;
 font-size: 25px;
 color: white;
 border-radius: 10px;
}

</style>
