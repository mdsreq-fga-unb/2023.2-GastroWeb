<template lang="pug">
q-page
  section.q-pa-xl.row.column
    q-input(
      bg-color="white"
      rounded
      color="grey"
      outlined
      borderless
      placeholder="Pesquise uma receita"
      v-model="texto"
    )
    q-btn(@click="mudarPagina" color="white" text-color="black").btn Criar Receita
  
</template>

<script>


export default {
  name: 'BuscaReceita',
  components: {},
  data(){
    return{
    }
  },
  methods:{
    mudarPagina(){
      this.$router.push({
          path: '/criarreceita'
      })
    }
  }
}
</script>
<style lang="sass">
.busca
  display: flex
  width: 100%

.btn
  margin: 15px
</style>
