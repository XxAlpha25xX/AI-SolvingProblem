<template>
  <div class="global">
    <div class="form-group">
      <span>{{ type }}</span>
      <input v-model="valueInput" class="form-field" type="number" :placeholder="placeholder">
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
export default class Input extends Vue {
  @Prop({ default: '' })
    placeholder!: string

  @Prop({ default: '' })
    default!: string

  @Prop({ default: '' })
    type!: string

  @Prop({ default: '' })
    updateParent!: Function

  valueInput = ''

  @Watch('valueInput')
  onValueChange () {
    this.$emit('updateValueInput', parseInt(this.valueInput), this.type)
  }

  mounted () {
    window.addEventListener('DOMContentLoaded', () => {

    })
  }
}
</script>

<style lang="scss" scoped>
  .form-group {
    display: flex;
    flex-direction: row;
    border-radius: 2px;
    height: 40px;
    margin-top: 30px;
    align-items: center;
    overflow: hidden;
    border-color: lightgray;
    border-width: 1px;
    border-style: solid;
    border-radius: 4px;
    transition: 0.5s all;

    &:focus, &:active, &:focus-within {
      border-color: #6300ff;
      border-radius: 4px;
      border-width: 2px;
    }

    span {
      padding: 5px 12px;
      background: #EEF4FF;
    }

    font-size:20px;
    input {
      border: none;
      padding:  7px 10px;
      outline: 0 none;
      height: 40px;
      background: white;
      font-size:20px;
      width: 130px;
    }
  }
</style>
