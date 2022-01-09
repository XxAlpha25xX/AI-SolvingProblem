<template>
  <div class="global">
    <div class="sub-global">
      <div class="title-box">
        <span class="title">{{ title }}</span>
      </div>
      <div class="dropdown">
        <div class="drop-btn">
          {{ picked }}
        </div>
        <div class="dropdown-content">
          <div v-for="line in arr" :key="line">
            <p :line="line" @click="pick(line)">
              {{ line }}
            </p>
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
  //  Watch,
  Vue
} from 'nuxt-property-decorator'

@Component
export default class DropDown extends Vue {
  @Prop({ default: '' })
    title!: string

  @Prop({ default: [] })
    arr!: string[]

  @Prop({ default: '' })
    picked! : string

  @Prop({ default: '' })
    type! : string

  mounted () {
    window.addEventListener('DOMContentLoaded', () => {

    })
  }

  pick (item: string) {
    this.$emit('pick', item, this.type)
  }
}
</script>

<style lang="scss" scoped>

  .global {
    display: flex;
    flex-direction: row;
    border: none;

    span {
      display: inline-block;
      font-size: 30px;
      background: #EEF4FF;
      height: 100%;
      padding: 5px 10px;
      height: 40px;
    }

    .sub-global {
      height: auto;
      border-width: 1px;
      border-style: solid;
      border-color: lightgray;
      border-radius: 5px;
      transition: 0.5s all;
      display: flex;
      justify-content: center;
      align-items: center;

      .title-box {
        display: flex;
        align-items: center;
        border-radius: 4px 0px 0px 4px;
        height: 100%;
        background: #EEF4FF;
      }
      .title {
        font-size: 20px;
        height: fit-content;
      }
    }
  }

  .dropdown {
    position: relative;
    display: inline-block;
    background: #6300ff;
    font-size:20px;
    color: white;
    transition: 0.5s all;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 0 4px 4px 0;
    height: 40px;
    &:hover {
      background: rgb(16, 153, 73);
    }
    cursor: pointer;
    padding: 5px 10px;
  }

  .dropdown-content {
    display: none;
    position: absolute;
    border-radius: 5px;
    top: 100%;
    background-color: #f9f9f9;
    min-width: 100px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    padding: 0px 0px;
    z-index: 1;

    p {
      padding: 4px 10px;
      color: black;
      font-size:20px;
      &:hover {
        background: lightgrey;
        cursor: pointer;
      }
    }
  }

  .drop-btn {
    height: fit-content;
  }

  .dropdown:hover .dropdown-content {
    display: flex;
    flex-direction: column;
  }
</style>
