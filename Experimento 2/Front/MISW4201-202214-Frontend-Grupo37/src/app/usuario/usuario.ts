export class Usuario {
    id: number;
    nombre: string;
    usuario: string;
    email: string;
    contrasena: string;
    rol: boolean;
    no_cuenta:string;
    nombre_banco: string;
    saldo:number;
    medio_pago: string;
    EventoDeportivos: Array<any>

    constructor(
        id: number,
        nombre: string,
        usuario: string,
        email: string,
        contrasena: string,
        rol: boolean,
        no_cuenta:string,
        nombre_banco: string,
        saldo:number,
        medio_pago: string,
        EventoDeportivos: Array<any>,
    ) {
        this.id = id;
        this.nombre = nombre;
        this.usuario = usuario;
        this.email = email;
        this.contrasena = contrasena;
        this.rol = rol;
        this.no_cuenta = no_cuenta;
        this.nombre_banco = nombre_banco;
        this.saldo = saldo;
        this.medio_pago = medio_pago;
        this.EventoDeportivos = EventoDeportivos;
    }
}
