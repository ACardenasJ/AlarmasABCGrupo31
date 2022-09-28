import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class UsuarioService {

    //private backUrl: string = "http://127.0.0.1:5000"
    private backUrl: string = environment.baseUrl;

    constructor(private http: HttpClient) { }

    userLogIn(usuario: string, contrasena: string): Observable<any> {
        return this.http.post<any>(`${this.backUrl}/login`, { "usuario": usuario, "contrasena": contrasena });
    }

    userSignUp(usuario: string, contrasena: string, correo: string, phone: string): Observable<any> {
        return this.http.post<any>(`${this.backUrl}/signin/user`, { "usuario": usuario, "u_email": correo, "contrasena": contrasena, "phone": phone })
    }
}
