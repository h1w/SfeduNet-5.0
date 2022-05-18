<template>
  <div style="margin-top: 1em !important">
    <div class="container">
      <h6 id="page-title">Контакты</h6>
      <div class="row">
        <!-- Start col -->
        <div class="col-lg-6">
          <div class="card m-b-30">
            <div class="card-body py-5">
              <div class="row">
                <div class="col-lg-3 text-center">
                  <img :src="contacts_1" class="img-fluid mb-3" alt="user" />
                </div>
                <div class="col-lg-8">
                  <h4>Дмитрий Елькин</h4>
                  <div class="table-responsive">
                    <table class="table table-borderless mb-0">
                      <tbody>
                        <tr>
                          <th scope="row" class="p-1">Должность:</th>
                          <td class="p-1">Руководитель проекта</td>
                        </tr>
                        <tr>
                          <th scope="row" class="p-1">VK:</th>
                          <td class="p-1"><a href="https://vk.com/kolokchik/" target="_blank">vk.com/kolokchik</a></td>
                        </tr>
                        <tr>
                          <th scope="row" class="p-1">Telegram:</th>
                          <td class="p-1"><a href="https://t.me/kolokchik/" target="_blank">t.me/kolokchik</a></td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- End col -->

        <!-- Start col -->
        <div class="col-lg-6">
          <div class="card m-b-30">
            <div class="card-body py-5">
              <div class="row">
                <div class="col-lg-3 text-center">
                  <img :src="contacts_2" class="img-fluid mb-3" alt="user" />
                </div>
                <div class="col-lg-8">
                  <h4>Даниил Кочубей</h4>
                  <div class="table-responsive">
                    <table class="table table-borderless mb-0">
                      <tbody>
                        <tr>
                          <th scope="row" class="p-1">Должность:</th>
                          <td class="p-1">Тимлид</td>
                        </tr>
                        <tr>
                          <th scope="row" class="p-1">VK:</th>
                          <td class="p-1"><a href="https://vk.com/id177176834" target="_blank">vk.com/id177176834</a></td>
                        </tr>
                        <tr>
                          <th scope="row" class="p-1">Telegram:</th>
                          <td class="p-1"><a href="https://t.me/Zimusss" target="_blank">t.me/Zimusss</a></td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- End col -->
    
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactsView',
  data: function () {
    return {
      contacts_1: require('@/assets/images/contacts/1.jpg'),
      contacts_2: require('@/assets/images/contacts/2.jpg'),
    }
  },
}
</script>

<style scoped>
#page-title {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 25px;
  line-height: 30px;
  text-align: center;
  margin-bottom: 1.5em;
}

body{
    background:#f2f3f7;
    margin-top:20px;
    }
.m-b-30 {
    margin-bottom: 30px;
}
p{
color: #8A98AC;
font-family: 'Inter';
font-style: normal;
}
.table-borderless td {
    border: 0 !important;
}
.table td {
    color: #8A98AC;
    vertical-align: middle;
    border-top: 1px solid rgba(0, 0, 0, 0.03);
    padding: 0.6rem;
}
.btn-primary-rgba {
    background-color: rgba(80, 111, 228, 0.1);
    border: none;
    color: #506fe4;
}
.btn-success-rgba {
    background-color: rgba(67, 209, 135, 0.1);
    border: none;
    color: #43d187;
}
.card {
    border: none;
    border-radius: 3px;
    background-color: #ffffff;
}
</style>