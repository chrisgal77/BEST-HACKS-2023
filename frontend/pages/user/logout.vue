<template>
  <div></div>
</template>

<script>
export default {
  mounted() {
    if (typeof window !== 'undefined') {
      document.cookie = 'token='
      document.cookie = 'user='
    }
    window.location.replace('../../')
  },
}
</script>
