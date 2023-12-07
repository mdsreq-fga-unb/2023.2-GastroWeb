const routes = [
  // {
  //   path: '/erro',
  //   component: () => import('layouts/MainLayout.vue'),
  //   children: [
  //     { path: '', component: () => import('pages/IndexPage.vue') }
  //   ]
  // },
  {
    path: '/',
    component: () => import('src/layouts/Principal.vue'),
    props: route => ({
      titulo: route.query.titulo,
      id: route.query.id,
      tags: route.query.tags,
      categorias: route.query.categorias
    }),
    children: [
      { path: '', name: 'pg_busca', component: () => import('src/pages/BuscaReceita.vue'), props: true },
      { path: '/receitas', name: 'pg_receitas', component: () => import('src/pages/ListaReceitas.vue'), props: true },
      { path: '/criarreceita', name: 'pg_criar_receita', component: () => import('src/pages/CriarReceita.vue') },
      { path: '/administrador', name: 'pg_usuario', component: () => import('src/pages/GerenciarReceitas.vue') },
      { path: '/exibirreceita', name: 'pg_receita', component: () => import('src/pages/TelaReceita.vue'), props: true }

    ]
  },
  {
    path: '/login',
    component: () => import('src/layouts/Fundo.vue'),
    children: [
      {
        path: '',
        name: 'pg_login',
        component: () => import('src/pages/TelaLogin.vue')
      }
    ]
  }

  // Always leave this as last one,
  // but you can also remove it
  // {
  //   path: '/:catchAll(.*)*',
  //   component: () => import('pages/ErrorNotFound.vue')
  // }
]

export default routes
