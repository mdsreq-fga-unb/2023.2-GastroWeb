<template lang="pug">
q-page
  section.q-pa-xl.column.gap
    li(@click="voltarPagina").row.secao-voltar
        q-icon(name="mdi-arrow-left-circle").q-mt-xs.icone-triangulo
        a.botao-voltar Voltar
    div.column
        span Título
        q-input(
            bg-color="white"
            rounded
            color="grey"
            outlined
            borderless
            placeholder="Digite o título da receita"
            v-model="texto"
        )
    div.column
        span Ingredientes:
        div(v-for="(ingrediente, index) in aux.ingredientes")
            q-input(
                bg-color="white"
                rounded
                color="grey"
                outlined
                borderless
                placeholder="Digite o ingrediente"
                v-model="texto"
            ).q-pb-sm
        q-btn(rounded flat color="white" no-caps @click="addIngrediente").btn Adicionar Ingrediente
    div.column
        span Modo de Preparo:
        q-input(
            bg-color="white"
            rounded
            color="grey"
            outlined
            borderless
            placeholder="Detalhe o mode de preparo"
            v-model="texto"
            type="textarea"
        ).q-pb-md
    div.column
        span Fotos:
        div(v-for="(foto, index) in aux.fotos")
            q-uploader(
            field-name="arquivo"
            :url="salvarFotoUrl"
            style="max-width: 354px;"
            color="white"
            text-color="black"
            flat
            accept=".jpg, .png, .jpeg, .pdf, image/*"
            max-files-size="50000000"
            max-file="1"
        ).q-ma-sm
        q-btn(rounded flat color="white" no-caps @click="addFoto").btn Adicionar mais imagens
  
</template>

<script>


export default {
  name: 'CriarReceita',
  components: {},
  data(){
    return{
      aux:{
        ingredientes: [],
        fotos: []
      }
    }
  },
  methods:{
    mudarPagina(){
      this.$router.push({
        path: '/criarreceita'
      })
    },
    voltarPagina(){
      this.$router.push({
        path: '/'
      })
    },
    addIngrediente(){
      this.aux.ingredientes.push('')
    },
    addFoto(){
      this.aux.fotos.push('')
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
  width: 250px
  background-color: black
  text-color: white

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

.gap
    gap: 20px
</style>
