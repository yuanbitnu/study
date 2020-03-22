<template>
    <div>
        <h1>company</h1>
    </div>
</template>
<script>
export default {
  data () {
    return {

    }
  },
  created () {
    this.$store.dispatch('setIsTab')
  }
}
</script>
<style lang="lsss" scoped>

</style>
