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
    div.row.checkbox
      div.column
        span Categorias
        div.caixa-branca.column
          q-checkbox(
            v-for="val in categorias"
            size="xs"
            v-model="aux.categorias"
            :val="val"
            :label="val"
          )
      div.column 
        span Tags
        div.caixa-branca.column
          q-checkbox(
            v-for="val in tags"
            size="xs"
            v-model="aux.tags"
            :val="val"
            :label="val"
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
          placeholder="Digite a porção e o ingrediente"
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
        placeholder="Detalhe o modo de preparo"
        type="textarea"
      ).q-pb-md
    div.column
      span Fotos:
      div(v-for="(file, index) in aux.files")
        input(type="file" :id="`fileInput${index + 1}`" accept="image/*")
      q-btn(rounded flat color="white" no-caps @click="addFoto").btn Adicionar Foto 
      q-btn(rounded flat color="white" no-caps @click="cadastrarReceita").btn Salvar Receita 
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
        categorias: [],
        tags: [],
        files: []
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
      ]
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
      let formData = new FormData()
      formData.append('titulo', this.aux.titulo)
      formData.append('ingredientes', this.transformarLista(this.aux.ingredientes))
      formData.append('instrucoes', this.aux.instrucoes)
      formData.append('categorias', this.transformarLista(this.aux.categorias))
      formData.append('tags', this.transformarLista(this.aux.tags))
      for (let i = 0; i < this.aux.files.length; i++) {
        const fileInput = document.getElementById(`fileInput${i + 1}`)
        formData.append('files', fileInput.files[0])
        console.log(fileInput.file)
      }
      console.log(formData)
      createRecipe(formData).then(() => {
        this.triggerMensagem('positive', 'Receita cadastrada.')
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
    },
    transformarLista(lista){
      return lista.join(',')
    }
  }
}
</script>
<style lang="sass" scoped>
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

.caixa-branca
  background-color: white
  border-radius: 20px
  padding: 20px
  height: 250px
  width: 200px

.checkbox
  gap: 30px
</style>
