<template lang="pug">
q-page
  section.q-pa-xl.column
    li(@click="voltarPagina").row.secao-voltar
      q-icon(name="mdi-arrow-left-circle").q-mt-xs.icone-triangulo
      a.botao-voltar Voltar
    CardReceita
</template>

<script>
import CardReceita from '../components/CardReceita.vue'

export default {
  name: 'ListaReceitas',
  components: { CardReceita },
  data(){
    return{
    }
  },
  methods:{
    voltarPagina(){
      this.$router.push({
        path: '/'
      })
    }
  }
}
</script>
<style lang="sass">
.secao-voltar
  gap: 5px
  cursor: pointer

.botao-voltar
  font-weight: 700
  color: white
  font-size: 15px
  line-hegiht: 18px
  height: 20px
  text-decoration: none

.icone-triangulo
    color: white
    size: 50px

</style>
