import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
Vue.config.productionTip = false

    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
import 'bootstrap'
new Vue({
  render: h => h(App),
}).$mount('#app')
