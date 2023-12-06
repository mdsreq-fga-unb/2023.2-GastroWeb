<template lang="pug">
q-page
  section.q-pa-xl.column.pagina
    div.items-left
      li(@click="voltarPagina").row.secao-voltar
        q-icon(name="mdi-arrow-left-circle").q-mt-xs.icone-triangulo
        a.botao-voltar Voltar
    div.column
      span Título
      q-input(
        bg-color="white"
        v-model="aux.titulo"
        rounded
        color="grey"
        outlined
        borderless
        placeholder="Digite o título da receita"
      )
    div.column
      span Ingredientes:
      div(v-for="(ingrediente, index) in aux.ingredientes")
        q-input(
          bg-color="white"
          v-model="aux.ingredientes[index]"
          rounded
          color="grey"
          outlined
          borderless
          placeholder="Digite o ingrediente"
        ).q-pb-sm
      q-btn(rounded flat color="white" no-caps @click="addIngrediente").btn Adicionar Ingrediente
    div.column
      span Modo de Preparo:
      q-input(
        bg-color="white"
        v-model="aux.instrucoes"
        rounded
        color="grey"
        outlined
        borderless
        placeholder="Detalhe o mode de preparo"
        type="textarea"
      ).q-pb-md
    div.column
      span Fotos:
      q-uploader(
        field-name="aux.files"
        :url="cadastrarReceita"
        style="max-width: 354px;"
        color="white"
        text-color="black"
        flat
        accept=".jpg, .png, .jpeg, .pdf, image/*"
        max-files-size="50000000"
        max-file="1"
        multiple
      ).q-ma-sm
    q-btn(rounded flat color="white" no-caps @click="cadastrarReceita").btn Cadastrar Receita
  
</template>

<script>
import { createRecipe } from '../services/recipe'

export default {
  name: 'CriarReceita',
  components: {},
  data(){
    return{
      aux:{
        titulo: '',
        ingredientes: [],
        instrucoes: '',
        categorias: ['JANTAR'],
        tags: ['PORCO'],
        files: ['aaaaa']
      }
    }
  },
  methods:{
    voltarPagina(){
      this.$router.push({
        path: '/administrador'
      })
    },
    addIngrediente(){
      this.aux.ingredientes.push('')
    },
    addFoto(){
      this.aux.files.push('')
    },
    verificarReceita(){
      return 'receita'
    },
    cadastrarReceita(){
      console.log(this.aux)
      createRecipe({
        ingredientes: this.aux.ingredientes,
        titulo: this.aux.titulo,
        tags: this.aux.tags,
        categorias: this.aux.categorias,
        files: this.aux.files,
        instrucoes: this.aux.instrucoes
      }).then(({ data }) => {
        this.triggerMensagem('positove', 'Receita cadastrada.')
        this.voltarPagina()
      }).catch(error => {
        console.log(error)
        this.triggerMensagem('negative', 'Não foi possível cadastrar receita.')
      })
    },
    triggerMensagem (type, menssage) {
      this.$q.notify({
        type: type,
        message: menssage
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

.pagina
  gap: 20px
  // display: flex
  // align-items: center
</style>
