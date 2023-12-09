<template lang="pug">
q-header.header.justify-between
  section.section-left.items-center.justify-center.alinhamento
    img(src="~assets/logo.png" @click="paginaInicial").size-logo.cursor-pointer
  div(v-if="!(nomePagina === 'pg_criar_receita' || nomePagina === 'pg_usuario')" @click="login").row.q-pr-md.items-center.cursor-pointer
    q-avatar(text-color="white" icon="mdi-login" @click="login")
</template>

<script>

export default {
  name: 'CabecalhoPrincipal',
  data(){
    return{
    }
  },
  computed: {
    nomePagina(){
      return this.$router.currentRoute.value.name
    }
  },
  methods:{
    paginaInicial(){
      this.$router.push({
        path: '/'
      })
    },
    login(){
      this.$router.push({
        path: '/login'
      })
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