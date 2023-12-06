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
    q-btn(@click="buscar" color="white" text-color="black" no-caps).btn Buscar
  
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
    buscar(){
      this.$router.push({
        path: '/receitas'
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
