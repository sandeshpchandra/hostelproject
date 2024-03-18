from django.urls import path

from AdminApp import views

urlpatterns=[
    path('index/',views.index,name="index"),


    path('adddepartment/',views.adddepartment,name="adddepartment"),
    path('savedepartment/',views.savedepartment,name="savedepartment"),
    path('displaydepartment/',views.displaydepartment,name="displaydepartment"),
    path('editdepartment/<int:dataid>', views.editdepartment, name="editdepartment"),
    path('updatedepartment/<int:dataid>', views.updatedepartment, name="updatedepartment"),
    path('deletedepartment/<int:dataid>',views.deletedepartment,name="deletedepartment"),

    path('addroom/', views.addroom, name="addroom"),
    path('saveroom/', views.saveroom, name="saveroom"),
    path('displayroom/', views.displayroom, name="displayroom"),
    path('editroom/<int:dataid>', views.editroom, name="editroom"),
    path('updateroom/<int:dataid>', views.updateroom, name="updateroom"),
    path('deleteroom/<int:dataid>', views.deleteroom, name="deleteroom"),

    path('addstudent/', views.addstudent, name="addstudent"),
    path('savestudent/', views.savestudent, name="savestudent"),
    path('displaystudent/', views.displaystudent, name="displaystudent"),
    path('editstudent/<int:dataid>', views.editstudent, name="editstudent"),
    path('updatestudent/<int:dataid>', views.updatestudent, name="updatestudent"),
    path('deletestudent/<int:dataid>', views.deletestudent, name="deletestudent"),

    path('complaints/', views.complaints, name="complaints"),
    path('deletecom/<int:dataid>', views.deletecom, name="deletecom"),

    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),

]