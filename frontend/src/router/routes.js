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
    children: [
      { path: 'busca', name: 'pg_busca', component: () => import('src/pages/BuscaReceita.vue') }
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
