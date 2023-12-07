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
      v-model="busca.titulo"
    )
    q-btn(@click="buscarPorTitulo" color="white" text-color="black" no-caps :disable="busca.titulo === ''").btn Buscar
  
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'BuscaReceita',
  components: {},
  data(){
    return{
      busca: {
        titulo: '',
        tags: [],
        categorias: []
      }
    }
  },
  methods:{
    buscarPorTitulo(){
      const query = {
        titulo: this.busca.titulo
      }
      const path = '/receitas'
      this.$router.push({ path, query })
    },
    buscarPorTagsCategorias(){
      const query = {
        tags: this.busca.tags,
        tribunal: this.busca.categorias
      }
      const path = '/receitas'
      this.$router.push({ path, query })
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
