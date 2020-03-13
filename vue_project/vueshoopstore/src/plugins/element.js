/* eslint-disable import/no-duplicates */
import Vue from 'vue'
import { Button } from 'element-ui'
import { Form, FormItem } from 'element-ui'
import { Input } from 'element-ui'
import { Message, Container, Header, Aside, Main } from 'element-ui'
<<<<<<< HEAD
import { Menu, Submenu, MenuItem } from 'element-ui'
=======
import { Menu, Submenu, MenuItem, Breadcrumb, BreadcrumbItem, Card, Row, Col, Table, TableColumn, Switch, Tooltip, Pagination, Dialog, MessageBox

} from 'element-ui'
>>>>>>> a95a82a66dd7af3d0c0579e4b191463633e1d7e7

Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Container)
Vue.use(Header)
Vue.use(Aside)
Vue.use(Main)
Vue.use(Menu)
Vue.use(Submenu)
Vue.use(MenuItem)
<<<<<<< HEAD
Vue.prototype.$message = Message // Message需要挂载到Vue的原型上
=======
Vue.use(Breadcrumb)
Vue.use(BreadcrumbItem)
Vue.use(Card)
Vue.use(Row)
Vue.use(Col)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Switch)
Vue.use(Tooltip)
Vue.use(Pagination)
Vue.use(Dialog)
Vue.prototype.$message = Message // Message需要挂载到Vue的原型上
Vue.prototype.$messageBox = MessageBox
>>>>>>> a95a82a66dd7af3d0c0579e4b191463633e1d7e7
