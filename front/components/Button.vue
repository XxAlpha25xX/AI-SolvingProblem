<template>
  <div class="button" @click="onClick">
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
  Watch,
  Vue
} from 'nuxt-property-decorator'

@Component
export default class Button extends Vue {
  @Prop({ default: '' })
    text!: string

  @Prop({ default: '' })
    type!: string

  mounted () {
    window.addEventListener('DOMContentLoaded', () => {

    })
  }

  onClick () {
    this.$emit('onButtonClick', this.type)
  }
}
</script>

<style lang="scss" scoped>

.button {
  width: fit-content;
  padding: 10px;
  height: 40px;
  background: #6300ff;
  border-radius: 4px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: 0.2s all;
  box-shadow: 33px 29px 15px -3px rgba(0,0,0,0.1);
  color: white;
  font-size: 30px;
  cursor: pointer;
  position: relative;

  &:hover {
    background: royalblue;
    transform: scale(1.05);
    font-size: 30px;
  }

  &:active {
    background: green;
    scale: (0.9);
  }
}

</style>
