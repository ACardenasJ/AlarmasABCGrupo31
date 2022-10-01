import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { JwtHelperService } from "@auth0/angular-jwt";
import { ToastrService } from 'ngx-toastr';
import { UsuarioService } from '../usuario.service';



@Component({
  selector: 'app-usuario-signup',
  templateUrl: './usuario-signup.component.html',
  styleUrls: ['./usuario-signup.component.css']
})
export class UsuarioSignupComponent implements OnInit {

  helper = new JwtHelperService();
  usuarioForm: FormGroup;

  constructor(
    private usuarioService: UsuarioService,
    private formBuilder: FormBuilder,
    private router: Router,
    private toastr: ToastrService
  ) { }

  ngOnInit() {
    this.usuarioForm = this.formBuilder.group({
      usuario: ["", [Validators.required, Validators.maxLength(50)]],
      password: ["", [Validators.required, Validators.maxLength(50), Validators.minLength(4)]],
      confirmPassword: ["", [Validators.required, Validators.maxLength(50), Validators.minLength(4)]],
      u_email: ["", [Validators.required, Validators.maxLength(50),Validators.pattern("^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$")]],
      u_phone: ["", [Validators.required, Validators.maxLength(10),Validators.pattern("^[0-9]*$")]]
    })
  }

  registrarUsuario() {
    this.usuarioService.userSignUp(this.usuarioForm.get('usuario')?.value,
    this.usuarioForm.get('password')?.value,
    this.usuarioForm.get('u_email')?.value,
    this.usuarioForm.get('u_phone')?.value)
      .subscribe(res => {
        const decodedToken = this.helper.decodeToken(res.token);
        this.router.navigate([`/main/${decodedToken.sub}/${res.token}`])
        this.showSuccess()
      },
      error => {
        if(error.error){
          //this.showError(`Ha ocurrido un error: ${error.error}`)
        }
        //console.log(error)
        this.showError(`Ha ocurrido un error: ${error.message}`)
      })
  }
  onRegisterD(){
    var btnRegistrarDisabled = (<HTMLInputElement> document.getElementById("btnRegistrar")).disabled;
    if(btnRegistrarDisabled){
      this.toastr.error("LOS CAMPOS ESTAN VACIOS, VUELVA A INTENTAR", "Error",{
        timeOut: 2000,
      })
    }
  }
  showError(error: string) {
    this.toastr.error(error, "Error")
  }

  showSuccess() {
    this.toastr.success(`Se ha registrado exitosamente`, "Registro exitoso");
  }

}
