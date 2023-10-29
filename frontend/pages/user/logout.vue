<template>
  <div></div>
</template>

<script>
export default {
  mounted() {
    if (typeof window !== 'undefined') {
      document.cookie = 'user_id='
    }
    window.location.replace('../../')
  },
}
</script>
