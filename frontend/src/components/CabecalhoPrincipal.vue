<template lang="pug">
q-header.header
    section.section-left.items-center.justify-center.alinhamento
      img(src="~assets/logo.png").size-logo
</template>

<script>

export default {
  name: 'CabecalhoPrincipal',
  data(){
    return{
    }
  }
}

</script>
<style lang="sass" scoped>
.header
  display: flex
  background-color: #A15D4F
  height: 60px

.size-logo
  height: 33px

.alinhamento
  display: flex

</style>