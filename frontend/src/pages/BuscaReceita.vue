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
    //- q-btn Buscar
  
</template>

<script>


export default {
  name: 'BuscaReceita',
  components: {},
  data(){
    return{
    }
  }
}
</script>
<style lang="sass">
.busca
  display: flex
  width: 100%
</style>
