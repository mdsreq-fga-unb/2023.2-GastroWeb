<template lang="pug">
q-page
  section.q-pa-xl.column
    div(v-if="!buscaCheckbox").column.caixa-branca
      q-input(
        bg-color="#D9D9D9"
        rounded
        color="grey"
        outlined
        borderless
        placeholder="Pesquise uma receita"
        v-model="busca.titulo"
        @keyup.enter="buscarPorTitulo"
      ).busca
      div.btn-container
        q-btn(@click="buscarPorTitulo" color="black" text-color="white" no-caps :disable="busca.titulo === ''").btn Buscar
    div(v-else).column.caixa-branca
      div.row.checkbox
        div.column
          span Categorias
          q-radio(
            v-for="val in categorias"
            size="xs"
            v-model="selecionados.categorias"
            :val="val"
            :label="value[val]"
            color="grey"
          )
        div.column 
          span Tags
          q-radio(
            v-for="val in tags"
            size="xs"
            v-model="selecionados.tags"
            :val="val"
            :label="value[val]"
            color="grey"
          )
      q-btn(@click="buscarPorTagsCategorias" color="black" text-color="white" no-caps :disable="!(selecionados.tags.length > 0 ||  selecionados.categorias.length > 0)").btn Buscar
    div.q-pt-lg
      span(
        v-if="!buscaCheckbox"
        @click="buscaCheckbox=!buscaCheckbox"
        class="custom-span"
      ).cursor-pointer Pesquisa por Tag e Categoria
      span(
        v-else
        @click="buscaCheckbox=!buscaCheckbox"
        class="custom-span"
      ).cursor-pointer Pesquisa por Título
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'BuscaReceita',
  components: {},
  data(){
    return{
      busca: {
        titulo: ''
      },
      buscaCheckbox: false,
      selecionados: {
        tags: [],
        categorias: []
      },
      tags: [
        'LACTOSE',
        'OLEAGINOSAS',
        'PORCO',
        'CARNE',
        'GLUTEN',
        'FRUTOSDOMAR'
      ],
      categorias: [
        'CAFE_DA_MANHA',
        'JANTAR',
        'ALMOCO',
        'DOCES',
        'LANCHE'
      ],
      value: {
        CAFE_DA_MANHA: 'Café da manhã',
        JANTAR: 'Jantar',
        ALMOCO: 'Almoço',
        DOCES: 'Doces',
        LANCHE: 'Lanche',
        LACTOSE: 'Lactose',
        OLEAGINOSAS: 'Oleaginosas',
        PORCO: 'Porco',
        CARNE: 'Carne',
        GLUTEN: 'Glúten',
        FRUTOSDOMAR: 'Frutos do mar'
      }
    }
  },
  methods:{
    ...mapActions('busca', ['setParametrosBusca']),
    buscarPorTitulo(){
      this.setParametrosBusca({
        titulo: this.busca.titulo || ''
      })
      const query = {
        titulo: this.busca.titulo
      }
      const path = '/receitas'
      this.$router.push({ path, query })
    },
    buscarPorTagsCategorias(){
      this.setParametrosBusca({
        tags: this.arrayfy(this.selecionados.tags),
        categorias: this.arrayfy(this.selecionados.categorias)
      })
      const query = {
        tags: this.selecionados.tags,
        categorias: this.selecionados.categorias
      }
      const path = '/receitas'
      this.$router.push({ path, query })
    },
    arrayfy (data) {
      return data
        ? Array.isArray(data)
          ? data
          : [ data ]
        : []
    }
  },
  mounted(){
    this.setParametrosBusca({
      titulo: '',
      tags: [],
      categorias: [],
      id: 0
    })
  }
}
</script>
<style lang="sass" scoped>
.busca
  display: flex
  width: 702px

.btn-container
  display: flex
  justify-content: center
  margin-top: 20px

.btn
  margin: 15px
  width: 200px
  border-radius: 50px
  

.checkbox
  gap: 100px
  justify-content: center

.caixa-branca
  background-color: white
  border-radius: 20px
  padding: 20px
  height: 310px
  align-items: center
  justify-content: center

.q-pt-lg
  display: flex
  justify-content: center

.custom-span
  display: inline-block
  padding: 8px 16px
  border: 1px solid #A15D4F
  background-color: #A15D4F
  color: #fff
  border-radius: 50px
  cursor: pointer
  transition: background-color 0.3s, color 0.3s, border-color 0.3s

.custom-span:hover
  background-color: #A15D4F
  border-color: #A15D4F
</style>
