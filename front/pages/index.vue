<template>
  <div class="global">
    <div class="menu">
      <div class="epitech">
        <img src="../assets/img/logo.png">
        <h3>- {Epitech}</h3>
      </div>
      <h1>Module - Artificial Intelligence: Problem solving</h1>
      <div class="card card-one">
        <div class="card-bg"></div>
        <img class="card-img" src="../assets/img/puzzle.jpg" />
        <div class="card-text">
          <p class="card-title">NPuzzle</p>
        </div>
      </div>
      <div class="card card-two">
        <div class="card-bg"></div>
        <img class="card-img" src="../assets/img/queen2.jpg" />
        <div class="card-text">
          <p class="card-title">NQueen</p>
        </div>
      </div>
      <div class="card card-three">
        <div class="card-bg"></div>
        <img class="card-img" src="../assets/img/brain.jpg" />
        <div class="card-text">
          <p class="card-title">Algorithm Used</p>
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
  //  Prop,
  //  Provide,
  //  Watch,
  Vue
} from 'nuxt-property-decorator'

@Component
export default class Index extends Vue {
  name = 'Stuff'
  timeout: any = null

  listenMouse () {
    const menu = (<HTMLElement>document.querySelector('.menu'))
    const images = document.querySelectorAll('.card-img')
    const range = 40

    const calcValue = (a:any, b:any) => (a / b * range - range / 2).toFixed(1)

    document.addEventListener('mousemove', ({ x, y }) => {
      if (this.timeout) {
        window.cancelAnimationFrame(this.timeout)
      }
      this.timeout = window.requestAnimationFrame(() => {
        const yValue = parseInt(calcValue(y, window.innerHeight))
        const xValue = parseInt(calcValue(x, window.innerWidth))

        if (menu === null) {
          console.log("[Error] menu is null")
          return
        }
        menu.style.transform = `rotateX(${-1 * yValue}deg) rotateY(${xValue}deg)`;
        [].forEach.call(images, (image: HTMLElement) => {
          image.style.transform = `translateX(${-xValue}px) translateY(${yValue}px)`
        });

      })
    }, false)
  }

  mounted () {
    window.addEventListener('DOMContentLoaded', () => {
      this.listenMouse()
    })
  }
}
</script>

<style lang="scss" scoped>
$logo-size:50px;

.global {
    display: flex;
    justify-content: center;
    height: 100vh;
    align-items: center;
    background-color: #b48bec;
    background-image: linear-gradient(135deg, #b48bec 0%, #6300ff 100%);

  h1 {
    color: #3e3e42;
    font-size:32px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 30px;
    transform: translateZ(35px);
    margin-top: 20px;
    font-family: 'Bebas Neue', cursive;
  }

  h3 {
    color: #eb285d;
    font-size: 16px;
    margin-bottom: 6px;
    transform: translateZ(25px);
    font-family: 'Bebas Neue', cursive;
  }

  .menu {
    background: #fff;
    border-radius: 15px;
    border-color: #6300ff;
    border-width: 8px;
    border-style: solid;
    box-shadow: 0px 10px 20px 20px rgba(0,0,0,0.17);
    display: inline-block;
    padding: 30px 35px;
    perspective: 1800px;
    text-align: left;
    transform-origin: 50% 50%;
    transform-style: preserve-3d;
    transform: rotateX(11deg) rotateY(16.5deg);
    min-width: 595px;
  }

  .epitech {
    display: flex;
    flex-direction: row;
    align-items: center;
    height: $logo-size;

    h3 {
      font-size: 50px;
      margin-left: 10px;
      color: royalblue;
      transform: translateY(5px) translateZ(25px);
    }
    img {
      width: $logo-size;
      height: $logo-size;
      transform: translateZ(25px);
    }
  }

  .card {
    border-radius: 15px;
    box-shadow: 5px 5px 20px -5px rgba(0,0,0,0.6);
    cursor: pointer;
    display: inline-block;
    height: 250px;
    overflow: hidden;
    perspective: 1200px;
    position: relative;
    transform-style: preserve-3d;
    transform: translateZ(35px);
    transition: transform 200ms ease-out;
    width: 175px;
    text-align: center;

    &:hover {
       box-shadow: 5px 5px 20px -7px rgba(0,0,0,0.5);
       transform: translateZ(60px) scale(1.1);
    }

    &:not(:last-child) {
      margin-right: 30px;
    }
  }

  .card-img {
    position: relative;
    height: 100%;
  }

  .card-bg {
    bottom: -50px;
    left: -50px;
    position: absolute;
    right: -50px;
    top: -50px;
    transform-origin: 50% 50%;
    transform: translateZ(-50px);
    z-index: 0;
  }

  .card-text {
    align-items: center;
    bottom: 0;
    display: flex;
    flex-direction: column;
    height: 70px;
    justify-content: center;
    position: absolute;
    width: 100%;
    z-index: 2;
  }

  .card-title {
    color: #fff;
    font-size: 18px;
    font-weight: 700;
    padding: 0 10px;
    margin-bottom: 3px;
  }

  .card-one {
    .card-img {
      top: -20px;
      right: 40px;
      height: 120%;
    }
  }

  .card-two {
    .card-img {
      top: -80px;
      right: 25px;
      height: 160%;
    }
  }

  .card-three {
    .card-img {
      top: -40px;
      right: 75px;
      height: 130%;
    }
  }
}


</style>
