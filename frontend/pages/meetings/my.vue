<template>
  <div class="gigantic-button">
    <nuxt-link to="./my1">
      <button class="discover-button" :style="{ background: backgroundColor }">
        Odkrywaj
      </button>
    </nuxt-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backgroundColor: '#ff5722', // Początkowy kolor tła
    }
  },
  mounted() {
    this.startColorAnimation()
  },
  beforeDestroy() {
    clearInterval(this.colorAnimationInterval)
  },
  methods: {
    startColorAnimation() {
      this.colorAnimationInterval = setInterval(() => {
        // Generowanie koloru sinusoidalnie
        const time = new Date().getTime()
        const red = Math.round(Math.sin(time / 1000) * 127 + 128)
        const green = Math.round(
          Math.sin(time / 1000 + (2 * Math.PI) / 3) * 127 + 128
        )
        const blue = Math.round(
          Math.sin(time / 1000 + (4 * Math.PI) / 3) * 127 + 128
        )

        this.backgroundColor = `rgb(${red}, ${green}, ${blue})`
      }, 1000 / 60)
    },
    discover() {
      window.location.replace('./my1')
    },
  },
}
</script>

<style scoped>
.gigantic-button {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.discover-button {
  font-size: 3em;
  padding: 20px 40px;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
}
</style>
