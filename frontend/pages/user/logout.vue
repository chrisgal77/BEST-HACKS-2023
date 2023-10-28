<template>
  <div></div>
</template>

<script>
export default {
  mounted() {
    if (typeof window !== 'undefined') {
      document.cookie = 'token='
    }
    window.location.replace('../../')
  },
}
</script>
