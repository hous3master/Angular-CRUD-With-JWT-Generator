import os

fatherDirectory = "C:/Users/cfmor/Documents/SI705_Arquitectura de Aplicaciones Web/backend automation"
projectName = "test"
# example of entities
"""
entities = [
    {
        "entityName": "Dessert",
        "attributes": [
            ["int", "idDessert"],
            ["String", "nameDessert"],
            ["LocalDate", "dueDateDessert"],
            ["String", "typeDessert"],
            ["int", "caloryDessert"],
        ],
    },
    {
        "entityName": "Ingredient",
        "attributes": [
            ["int", "idIngredient"],
            ["String", "nameIngredient"],
            ["double", "amountIngredient"],
            ["String", "typeIngredient"],
            ["Dessert", "dessert"],  # Many to one
        ],
    },
]
"""
# My entities
"""
"""

entities = [
    {
        "entityName": "Dessert",
        "attributes": [
            ["int", "idDessert"],
            ["String", "nameDessert"],
            ["LocalDate", "dueDateDessert"],
            ["String", "typeDessert"],
            ["int", "caloryDessert"],
        ],
    },
    {
        "entityName": "Ingredient",
        "attributes": [
            ["int", "idIngredient"],
            ["String", "nameIngredient"],
            ["double", "amountIngredient"],
            ["String", "typeIngredient"],
            ["Dessert", "dessert"],  # Many to one
        ],
    },
]


# Generate the environment file
def generateEnvironment(projectName):
    content = """
    export const environment = {
        production: false,
        base: "http://localhost:8080" // Ruta a la API
    }
    """

    # Create a folder called ProjectName/src/environments
    route = f"{projectName}/src/environments"
    fileName = "environment.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate the app.module.ts file
def generateAppModule(projectName):
    content = """
    import { HttpClientModule } from '@angular/common/http';
    import { NgModule } from '@angular/core';
    import { BrowserModule } from '@angular/platform-browser';
    import { AppRoutingModule } from './app-routing.module';
    import { AppComponent } from './app.component';
    import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
    import { MatToolbarModule } from '@angular/material/toolbar';
    import { FormsModule, ReactiveFormsModule } from '@angular/forms';
    import { MatInputModule } from '@angular/material/input';
    import { MatButtonModule } from '@angular/material/button';
    import { MatMenuModule } from '@angular/material/menu';
    import { MatIconModule } from '@angular/material/icon';
    import { LoginComponent } from './components/login/login.component';
    import { MatSnackBarModule } from '@angular/material/snack-bar';


    @NgModule({
    declarations: [
        AppComponent,
        LoginComponent,
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        BrowserAnimationsModule,
        MatIconModule,
        MatMenuModule,  
        MatButtonModule,
        MatInputModule,
        MatToolbarModule,
        FormsModule,
        ReactiveFormsModule,
        MatSnackBarModule,

    ],
    providers: [],
    bootstrap: [AppComponent]
    })
    export class AppModule { }
    """

    # Create a folder called ProjectName/src/app
    route = f"{projectName}/src/app"
    fileName = "app.module.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate components.module.ts file
def generateComponentsModule(projectName, entities):
    content = """
    import { MatDatepickerModule } from '@angular/material/datepicker';
    import { MatListModule } from '@angular/material/list';
    import { NgModule } from '@angular/core';
    import { CommonModule } from '@angular/common';
    import { ComponentsRoutingModule } from './components-routing.module';
    import { MatPaginatorModule } from '@angular/material/paginator';
    import { MatNativeDateModule } from '@angular/material/core';
    import { MatTableModule } from '@angular/material/table';
    import { MatSelectModule } from '@angular/material/select';
    import { FormsModule, ReactiveFormsModule } from '@angular/forms';
    import { MatInputModule } from '@angular/material/input';
    import { MatButtonModule } from '@angular/material/button';
    import { MatIconModule } from '@angular/material/icon';
    import { NgChartsModule } from 'ng2-charts';
    """

    # Import the components
    for entity in entities:
        content += f'import {{ {entity["entityName"]}Component }} from \'./{entity["entityName"].lower()}/{entity["entityName"].lower()}.component\';\n'
        content += f'import {{ Listar{entity["entityName"]}Component }} from \'./{entity["entityName"].lower()}/listar-{entity["entityName"].lower()}/listar-{entity["entityName"].lower()}.component\';\n'
        content += f'import {{ Creaedita{entity["entityName"]}Component }} from \'./{entity["entityName"].lower()}/creaedita-{entity["entityName"].lower()}/creaedita-{entity["entityName"].lower()}.component\';\n'

    content += """
    @NgModule({
    declarations: [
    """

    # Add the components to the declarations
    for entity in entities:
        content += f'{entity["entityName"]}Component,\n'
        content += f'Listar{entity["entityName"]}Component,\n'
        content += f'Creaedita{entity["entityName"]}Component,\n'

    content += """
    ],
    imports: [
        CommonModule,
        ComponentsRoutingModule,
        MatListModule,
        MatDatepickerModule,
        MatPaginatorModule,
        MatNativeDateModule,
        MatTableModule,
        MatSelectModule,
        FormsModule,
        ReactiveFormsModule,
        MatInputModule,
        MatButtonModule,
        MatIconModule,
        NgChartsModule
    ]
    })
    export class ComponentsModule { }
    """

    # Create a folder called ProjectName/src/app/components
    route = f"{projectName}/src/app/components"
    fileName = "components.module.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate entityname.ts model file
def generateEntityModel(projectName, entity):
    content = ""
    # import the entity foreign keys models
    for attribute in entity["attributes"]:
        if attribute[0].lower() not in ["string","int","double","localdate","boolean"]:
            content += f"import {{ {attribute[0]} }} from './{attribute[0].lower()}'\n"

    content += f'export class {entity["entityName"]} {{\n'

    # For each attribute
    for attribute in entity["attributes"]:
        # If is String
        if attribute[0] == "String":
            content += f'{attribute[1]}:string="";\n'
        # If is Int or Double
        elif attribute[0].lower() == "int" or attribute[0].lower() == "double":
            content += f"{attribute[1]}:number=0;\n"
        # If is LocalDate
        elif attribute[0].lower() == "localdate":
            content += f"{attribute[1]}:Date=new Date(Date.now());\n"
        # If is Boolean
        elif attribute[0].lower() == "boolean":
            content += f"{attribute[1]}:boolean=false;\n"
        # If is a Foreign Key
        else:
            content += f"{attribute[1]}:{attribute[0]}=new {attribute[0]}();\n"
    content += "}"

    # Create a folder called ProjectName/src/app/models
    route = f"{projectName}/src/app/models"
    fileName = f"{entity['entityName'].lower()}.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate entityname.service.ts file
def generateEntityService(projectName, entity):
    content = f"""
    import {{ {entity["entityName"]} }} from './../models/{entity["entityName"].lower()}';
    import {{ environment }} from './../../environments/environment';
    import {{ Injectable }} from '@angular/core';
    import {{ Observable, Subject }} from 'rxjs';
    import {{ HttpClient, HttpHeaders }} from '@angular/common/http';
    const base_url = environment.base;
    @Injectable({{
    providedIn: 'root',
    }})
    export class {entity["entityName"]}Service {{
    private url = `${{base_url}}/{entity["entityName"].lower()}`;
    private listaCambio = new Subject<{entity["entityName"]}[]>();
    constructor(private http: HttpClient) {{}}
    list() {{
        let token = sessionStorage.getItem('token');

        return this.http.get<{entity["entityName"]}[]>(this.url, {{
        headers: new HttpHeaders()
            .set('Authorization', `Bearer ${{token}}`)
            .set('Content-Type', 'application/json'),
        }});
    }}
    insert({entity["entityName"].lower()}: {entity["entityName"]}) {{
        let token = sessionStorage.getItem('token');

        return this.http.post(this.url, {entity["entityName"].lower()}, {{
        headers: new HttpHeaders()
            .set('Authorization', `Bearer ${{token}}`)
            .set('Content-Type', 'application/json'),
        }});
    }}
    setList(listaNueva: {entity["entityName"]}[]) {{
        this.listaCambio.next(listaNueva);
    }}
    getList() {{
        return this.listaCambio.asObservable();
    }}
    listId(id: number) {{
        let token = sessionStorage.getItem('token');

        return this.http.get<{entity["entityName"]}>(`${{this.url}}/${{id}}`, {{
        headers: new HttpHeaders()
            .set('Authorization', `Bearer ${{token}}`)
            .set('Content-Type', 'application/json'),
        }});
    }}
    update({entity["entityName"].lower()}: {entity["entityName"]}) {{
        let token = sessionStorage.getItem('token');

        return this.http.put(this.url, {entity["entityName"].lower()}, {{
        headers: new HttpHeaders()
            .set('Authorization', `Bearer ${{token}}`)
            .set('Content-Type', 'application/json'),
        }});
    }}
    delete(id: number) {{
        let token = sessionStorage.getItem('token');

        return this.http.delete(`${{this.url}}/${{id}}`, {{
        headers: new HttpHeaders()
            .set('Authorization', `Bearer ${{token}}`)
            .set('Content-Type', 'application/json'),
        }});
    }}
    }}
    """

    # Create a folder called ProjectName/src/app/services
    route = f"{projectName}/src/app/services"
    fileName = f"{entity['entityName'].lower()}.service.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate entity component typescript file
def generateEntityComponentTypescript(projectName, entity):
    content = f"""
    import {{ Component, OnInit }} from '@angular/core';
    import {{ ActivatedRoute, Router }} from '@angular/router';
    @Component({{
    selector: 'app-{entity["entityName"].lower()}',
    templateUrl: './{entity["entityName"].lower()}.component.html',
    styleUrls: ['./{entity["entityName"].lower()}.component.css'],
    }})
    export class {entity["entityName"]}Component implements OnInit {{
    constructor(public route: ActivatedRoute, public router: Router) {{}}
    ngOnInit(): void {{}}
    }}
    """

    # Create a folder called ProjectName/src/app/components/entityname
    route = f"{projectName}/src/app/components/{entity['entityName'].lower()}"
    fileName = f"{entity['entityName'].lower()}.component.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate entity component html file
def generateEntityComponentHtmlFile(projectName, entity):
    """<router-outlet></router-outlet>
    <div [hidden]="route.children.length !== 0">
    <app-listar-entityname></app-listar-entityname>
    </div>
    """

    content = f"""
    <router-outlet></router-outlet>
    <div [hidden]="route.children.length !== 0">
    <app-listar-{entity["entityName"].lower()}></app-listar-{entity["entityName"].lower()}>
    </div>
    """

    # Create a folder called ProjectName/src/app/components/entityname
    route = f"{projectName}/src/app/components/{entity['entityName'].lower()}"
    fileName = f"{entity['entityName'].lower()}.component.html"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a html file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate listar-entityname.component.ts file
def generateListarEntityTypescript(projectName, entity):
    """
    import { entityNameService } from './../../../services/entityName.service';
    import { entityName } from './../../../models/entityname';
    import { Component, OnInit, ViewChild } from '@angular/core';
    import { MatTableDataSource } from '@angular/material/table';
    import { MatPaginator } from '@angular/material/paginator';
    @Component({
    selector: 'app-listar-entityname',
    templateUrl: './listar-entityname.component.html',
    styleUrls: ['./listar-entityname.component.css'],
    })
    export class ListarentityNameComponent implements OnInit {
    dataSource: MatTableDataSource<entityName> = new MatTableDataSource();
    displayedColumns: string[] = ['attribute1','attribute2','attribute3','accion01','accion02'];
    @ViewChild(MatPaginator) paginator!: MatPaginator;
    constructor(private myService: entityNameService) {}

    ngOnInit(): void {
        this.myService.list().subscribe((data) => {
        this.dataSource = new MatTableDataSource(data);
        this.dataSource.paginator = this.paginator;
        });
        this.myService.getList().subscribe((data) => {
        this.dataSource = new MatTableDataSource(data);
        this.dataSource.paginator = this.paginator;

        }); 
    }
    eliminar(id: number) {
        this.myService.delete(id).subscribe((data) => {
        this.myService.list().subscribe((data) => {
            this.myService.setList(data);
        });
        });
    }
    filter(en: any) {
        this.dataSource.filter = en.target.value.trim();
    }
    }
    """

    content = f"""
    import {{ {entity["entityName"]}Service }} from './../../../services/{entity["entityName"].lower()}.service';
    import {{ {entity["entityName"]} }} from './../../../models/{entity["entityName"].lower()}';
    import {{ Component, OnInit, ViewChild }} from '@angular/core';
    import {{ MatTableDataSource }} from '@angular/material/table';
    import {{ MatPaginator }} from '@angular/material/paginator';
    @Component({{
    selector: 'app-listar-{entity["entityName"].lower()}',
    templateUrl: './listar-{entity["entityName"].lower()}.component.html',
    styleUrls: ['./listar-{entity["entityName"].lower()}.component.css'],
    }})
    export class Listar{entity["entityName"]}Component implements OnInit {{
    dataSource: MatTableDataSource<{entity["entityName"]}> = new MatTableDataSource();
    displayedColumns: string[] = ["""

    # For each attribute
    for attribute in entity["attributes"]:
        content += f"'{attribute[1]}',"

    content += f"""
    'accion01','accion02'];
    @ViewChild(MatPaginator) paginator!: MatPaginator;
    constructor(private myService: {entity["entityName"]}Service) {{}}

    ngOnInit(): void {{
        this.myService.list().subscribe((data) => {{
        this.dataSource = new MatTableDataSource(data);
        this.dataSource.paginator = this.paginator;
        }});
        this.myService.getList().subscribe((data) => {{
        this.dataSource = new MatTableDataSource(data);
        this.dataSource.paginator = this.paginator;

        }}); 
    }}
    eliminar(id: number) {{
        this.myService.delete(id).subscribe((data) => {{
        this.myService.list().subscribe((data) => {{
            this.myService.setList(data);
        }});
        }});
    }}
    filter(en: any) {{
        this.dataSource.filter = en.target.value.trim();
    }}
    }}
    """

    # Create a folder called ProjectName/src/app/components/entityname/listar-entityname
    route = f"{projectName}/src/app/components/{entity['entityName'].lower()}/listar-{entity['entityName'].lower()}"
    fileName = f"listar-{entity['entityName'].lower()}.component.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate listar-entityname.component.html file
def generateListarEntityHtml(projectName, entity):
    """
    <h2 style="text-align: center">entityName list</h2>
    <div style="text-align: right">
    <button mat-raised-button color="primary" routerLink="/postres/nuevo">
        Nuevo
    </button>
    </div>
    <mat-form-field>
    <input matInput (keyup)="filter($event)" placeholder="buscar" />
    </mat-form-field>

    <table mat-table [dataSource]="dataSource" class="mat-elevation-z8">

    <ng-container matColumnDef="attribute1">
        <th mat-header-cell *matHeaderCellDef>attribute1</th>
        <td mat-cell *matCellDef="let element">{{ element.attribute1 }}</td>
    </ng-container>
    <ng-container matColumnDef="attribute2">
        <th mat-header-cell *matHeaderCellDef>attribute2</th>
        <td mat-cell *matCellDef="let element">{{ element.attribute2 }}</td>
    </ng-container>
    <ng-container matColumnDef="attribute3">
        <th mat-header-cell *matHeaderCellDef>attribute3</th>
        <td mat-cell *matCellDef="let element">{{ element.attribute3 }}</td>
    </ng-container>

    <ng-container matColumnDef="accion01">
        <th mat-header-cell *matHeaderCellDef>actions</th>
        <td mat-cell *matCellDef="let element">
        <button mat-raised-button color="primary" [routerLink]="['ediciones', element.idEntityName]">
            <mat-icon>create</mat-icon>
        </button>
        </td>
    </ng-container>
    <ng-container matColumnDef="accion02">
        <th mat-header-cell *matHeaderCellDef>actions</th>
        <td mat-cell *matCellDef="let element">
        <button mat-raised-button color="warn" (click)="eliminar(element.idEntityName)">
            <mat-icon>delete</mat-icon>
        </button>
        </td>
    </ng-container>

    <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>
    <tr mat-row *matRowDef="let row; columns: displayedColumns"></tr>

    </table>
    <mat-paginator [pageSizeOptions]="[5, 10, 25, 100]" showFirstLastButtons></mat-paginator>
    """

    content = f"""
    <h2 style="text-align: center">{entity["entityName"]} list</h2>
    <button mat-raised-button color="primary" routerLink="/components/{entity["entityName"].lower()}/nuevo">
        Nuevo
    </button>
    <mat-form-field>
    <input matInput (keyup)="filter($event)" placeholder="buscar" />
    </mat-form-field>

    <table mat-table [dataSource]="dataSource" class="mat-elevation-z8">
    """

    # For each attribute that is not a foreign key
    for attribute in entity["attributes"]:
        if attribute[0].lower() in ["string","int","double","localdate","boolean"]:
            content += f"""
            <ng-container matColumnDef="{attribute[1]}">
                <th mat-header-cell *matHeaderCellDef>{attribute[1]}</th>
                <td mat-cell *matCellDef="let element">{{{{ element.{attribute[1]} }}}}</td>
            </ng-container>
            """
        else:
            content += f"""
            <ng-container matColumnDef="{attribute[1]}">
                <th mat-header-cell *matHeaderCellDef>{attribute[1]}</th>
                <td mat-cell *matCellDef="let element">{{{{ element.{attribute[1]}.id{attribute[0]}}}}}</td>
            </ng-container>
            """

    content += f"""
    <ng-container matColumnDef="accion01">
        <th mat-header-cell *matHeaderCellDef>actions</th>
        <td mat-cell *matCellDef="let element">
        <button mat-raised-button color="primary" [routerLink]="['ediciones', element.{entity["attributes"][0][1]}]">
            <mat-icon>create</mat-icon>
        </button>
        </td>
    </ng-container>
    <ng-container matColumnDef="accion02">
        <th mat-header-cell *matHeaderCellDef>actions</th>
        <td mat-cell *matCellDef="let element">
        <button mat-raised-button color="warn" (click)="eliminar(element.{entity["attributes"][0][1]})">
            <mat-icon>delete</mat-icon>
        </button>
        </td>
    </ng-container>
    """

    content += f"""
    <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>
    <tr mat-row *matRowDef="let row; columns: displayedColumns"></tr>

    </table>
    <mat-paginator [pageSizeOptions]="[5, 10, 25, 100]" showFirstLastButtons></mat-paginator>
    """

    # Create a folder called ProjectName/src/app/components/entityname/listar-entityname
    route = f"{projectName}/src/app/components/{entity['entityName'].lower()}/listar-{entity['entityName'].lower()}"
    fileName = f"listar-{entity['entityName'].lower()}.component.html"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a html file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate entity component creaedita typescript file
def generateEntityComponentCreaEditaTypescriptFile(projectName, entity):
    """import { Component, OnInit } from '@angular/core';
    import { ActivatedRoute, Params, Router } from '@angular/router';
    import * as moment from 'moment';
    import {
    FormGroup,
    FormControl,
    Validators,
    FormBuilder,
    AbstractControl,
    } from '@angular/forms';
    import { EntityName } from 'src/app/models/entityName';
    import { EntityNameService } from 'src/app/services/entityName.service';
    // For every foreign key attribute
    import { AttributeClass } from 'src/app/models/attributeClass';
    import { AttributeClassService } from 'src/app/services/attributeClass.service';
    @Component({
    selector: 'app-creaedita-entityName',
    templateUrl: './creaedita-entityName.component.html',
    styleUrls: ['./creaedita-entityName.component.css'],
    })
    export class CreaeditaEntityNameComponent implements OnInit {
    form: FormGroup = new FormGroup({});
    entityName: EntityName = new EntityName();
    mensaje: string = '';
    maxAttributeName: Date = moment().add(-1, 'days').toDate(); // NOTE: Only if there is an AttributeName of type LocalDate
    attributeName = new FormControl(new Date()); // NOTE: Only if there is an AttributeName of type LocalDate
    id: number = 0;
    edicion: boolean = false;
    // New to components with foreign keys
    listaAttributeClass:AttributeClass[]=[];

    constructor(
        private entityNameService: EntityNameService,
        private router: Router,
        private formBuilder: FormBuilder,
        private route: ActivatedRoute

        // New to components with foreign keys
        private attributeClassService: AttributeClassService
    ) {}

    ngOnInit(): void {
    
        this.route.params.subscribe((data: Params) => {
        this.id = data['id'];
        this.edicion = data['id'] != null;
        this.init();
        });

        // New to components with foreign keys
        this.attributeClassService.list().subscribe((data)=>{
        this.listaAttributeClass = data;
        })

        this.form = this.formBuilder.group({
        idEntityName: [''],
        // Validators for each attribute
        attributeName: ['', Validators.required],
        attributeName: ['', Validators.required],
        attributeName: ['', [Validators.required]],
        attributeName: ['', Validators.required],
        });
    }
    aceptar(): void {
        if (this.form.valid) {
        // Assign values to the entityName
        this.entityName.idEntityName = this.form.value.idEntityName;
        // Assign values to each attribute
        this.entityName.attributeName = this.form.value.attributeName;
        this.entityName.attributeName = this.form.value.attributeName;
        this.entityName.attributeName = this.form.value.attributeName;
        this.entityName.attributeName = this.form.value.attributeName;
        this.entityName.attributeClass.idAttributeClass = this.form.value.attributeClass; // Change for component with foreign keys
        this.entityName.attributeClass.idAttributeClass = this.form.value.attributeClass; // Change for component with foreign keys
        if (this.edicion) {
            this.entityNameService.update(this.entityName).subscribe(() => {
            this.entityNameService.list().subscribe((data) => {
                this.entityNameService.setList(data);
            });
            });
        } else {
            this.entityNameService.insert(this.entityName).subscribe((data) => {
            this.entityNameService.list().subscribe((data) => {
                this.entityNameService.setList(data);
            });
            });
        }
        this.router.navigate(['entityName']);
        } else {
        this.mensaje = 'Por favor complete todos los campos obligatorios.';
        }
    }

    obtenerControlCampo(nombreCampo: string): AbstractControl {
        const control = this.form.get(nombreCampo);
        if (!control) {
        throw new Error(`Control no encontrado para el campo ${nombreCampo}`);
        }
        return control;
    
    }
    init() {
        if (this.edicion) {
        this.entityNameService.listId(this.id).subscribe((data) => {
            this.form = new FormGroup({
            // Attributes of the formGroup
            idEntityName: new FormControl(data.idEntityName),
            attributeName: new FormControl(data.attributeName),
            attributeName: new FormControl(data.attributeName),
            attributeName:new FormControl(data.attributeName),
            attributeName: new FormControl(data.attributeName),
            attributeClass: new FormControl(data.attributeClass.idAttributeClass) // Change for component with foreign keys
            });
        });
        }
    }
    }
    """
    content = f"""
    import {{ Component, OnInit }} from '@angular/core';
    import {{ ActivatedRoute, Params, Router }} from '@angular/router';
    import * as moment from 'moment';
    import {{
        FormGroup,
        FormControl,
        Validators,
        FormBuilder,
        AbstractControl,
    }} from '@angular/forms';
    import {{ {entity["entityName"]} }} from '../../../models/{entity["entityName"].lower()}';
    import {{ {entity["entityName"]}Service }} from '../../../services/{entity["entityName"].lower()}.service';
    """
    
    # For any attribute that is a Foreign Key
    for attribute in entity['attributes']:
        if attribute[0].lower() not in ['string', 'int', 'double', 'localdate', 'boolean']:
            content += f'import {{ {attribute[0]} }} from \'../../../models/{attribute[0].lower()}\';\n'
            content += f'import {{ {attribute[0]}Service }} from \'../../../services/{attribute[0].lower()}.service\';\n'

    content += f"""
    @Component({{
        selector: 'app-creaedita-{entity["entityName"].lower()}',
        templateUrl: './creaedita-{entity["entityName"].lower()}.component.html',
        styleUrls: ['./creaedita-{entity["entityName"].lower()}.component.css'],
    }})
    export class Creaedita{entity["entityName"]}Component implements OnInit {{
        form: FormGroup = new FormGroup({{}});
        {entity["entityName"].lower()}: {entity["entityName"]} = new {entity["entityName"]}();
        mensaje: string = '';
    """

    # For any attribute of type LocalDate
    for attribute in entity['attributes']:
        if attribute[0].lower() == 'localdate':
            content += f'max{attribute[1]}: Date = moment().add(-1, \'days\').toDate();\n'
            content += f'{attribute[1]} = new FormControl(new Date());\n'
    
    content += """
    id: number = 0;
    edicion: boolean = false;
    """

    # For any attribute that is a Foreign Key
    for attribute in entity['attributes']:
        if attribute[0].lower() not in ['string', 'int', 'double', 'localdate', 'boolean']:
            content += f'lista{attribute[0]}: {attribute[0]}[]=[];\n'


    content += f"""
    constructor(
        private {entity["entityName"].lower()}Service: {entity["entityName"]}Service,
        private router: Router,
        private formBuilder: FormBuilder,
        private route: ActivatedRoute,
    """

    # For any attribute that is a Foreign Key
    for attribute in entity['attributes']:
        if attribute[0].lower() not in ['string', 'int', 'double', 'localdate', 'boolean']:
            content += f'private {attribute[0].lower()}Service: {attribute[0]}Service,\n'
    # delete last comma
    content = content[:-2]
    content += ') {}\n'

    content += f"""
    ngOnInit(): void {{
        this.route.params.subscribe((data: Params) => {{
            this.id = data['id'];
            this.edicion = data['id'] != null;
            this.init();
        }});
    """

    # For any attribute that is a Foreign Key
    for attribute in entity['attributes']:
        if attribute[0].lower() not in ['string', 'int', 'double', 'localdate', 'boolean']:
            content += f"""
            this.{attribute[0].lower()}Service.list().subscribe((data) => {{
                this.lista{attribute[0]} = data;
            }})
            """

    content += """
        this.form = this.formBuilder.group({
    """
    # Id attribute does not require validators
    content += f"""
            {entity['attributes'][0][1]}: [''],
    """

    for attribute in entity['attributes'][1:]:
        # Attribute require validators
        content += f"""
                    {attribute[1]}: ['', Validators.required],
        """

    content += f"""
        }});
    }}

    aceptar(): void {{
        if (this.form.valid) {{
    """

    # for each attribute
    for attribute in entity['attributes']: 
        if attribute[0].lower() in ['string', 'int', 'double', 'localdate', 'boolean']:
            content += f'this.{entity["entityName"].lower()}.{attribute[1]} = this.form.value.{attribute[1]};\n'
        else:
            content += f'this.{entity["entityName"].lower()}.{attribute[1]}.id{attribute[0]} = this.form.value.{attribute[1]}; // Change for component with foreign keys\n'
        
    content += f"""
            if (this.edicion) {{
                this.{entity["entityName"].lower()}Service.update(this.{entity["entityName"].lower()}).subscribe(() => {{
                    this.{entity["entityName"].lower()}Service.list().subscribe((data) => {{
                        this.{entity["entityName"].lower()}Service.setList(data);
                    }});
                }});
            }} else {{
                this.{entity["entityName"].lower()}Service.insert(this.{entity["entityName"].lower()}).subscribe((data) => {{
                    this.{entity["entityName"].lower()}Service.list().subscribe((data) => {{
                        this.{entity["entityName"].lower()}Service.setList(data);
                    }});
                }});
            }}
            this.router.navigate(['/components/{entity["entityName"].lower()}']);
        }}
        else {{
            this.mensaje = 'Por favor complete todos los campos obligatorios.';
        }}
        }}

        obtenerControlCampo(nombreCampo: string): AbstractControl {{
            const control = this.form.get(nombreCampo);
            if (!control) {{
                throw new Error(`Control no encontrado para el campo ${{nombreCampo}}`);
            }}
            return control;
        }}

    init() {{
        if (this.edicion) {{
            this.{entity["entityName"].lower()}Service.listId(this.id).subscribe((data) => {{
                this.form = new FormGroup({{
    """
    
    for attribute in entity['attributes']:
        if attribute[0].lower() in ['string', 'int', 'double', 'localdate', 'boolean']:
            content += f'{attribute[1]}: new FormControl(data.{attribute[1]}),\n'
        else:
            content += f'{attribute[1]}: new FormControl(data.{attribute[1]}.id{attribute[0]}), // Change for component with foreign keys\n'
    
    content += """
    });
    });
    }
    }
    }
    """

    # Create a folder called ProjectName/src/app/components/entityName/creaedita-entityName
    route = f"{projectName}/src/app/components/{entity['entityName'].lower()}/creaedita-{entity['entityName'].lower()}"
    fileName = f"creaedita-{entity['entityName'].lower()}.component.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate entity component creaedita html file
def generateEntityComponentCreaEditaHtmlFile(projectName, entity):
    content = f"""
    <h2>Registro de {entity["entityName"].lower()}</h2>
    <form [formGroup]="form" (submit)="aceptar()" class="example-form">
        <!-- idEntityName -->
    """
    content += f"""
        <mat-form-field class="example-full-width" *ngIf="edicion">
            <mat-label>{entity["attributes"][0][1]}</mat-label>
            <input matInput placeholder="Id" formControlName="{entity["attributes"][0][1]}"/>
        </mat-form-field>
        <br />
        <!-- Form fields for each attribute -->
    """
    for attribute in entity['attributes'][1:]:
        if attribute[0].lower() in ['string', 'int', 'double', 'boolean']:
            content += f"""
            <!-- NOTE : Only if is not of type LocalDate -->
            <mat-form-field class="example-full-width">
                <mat-label>{attribute[1]}</mat-label>
                <input matInput placeholder="{attribute[1]}" formControlName="{attribute[1]}"/>
                <mat-error *ngIf="obtenerControlCampo('{attribute[1]}')?.errors?.['required']">
                    {attribute[1]} es obligatorio.
                </mat-error>
            </mat-form-field>
            <br />
            """
        elif attribute[0].lower() == 'localdate':
            content += f"""
            <!-- NOTE : Only if is of type LocalDate -->
            <mat-form-field appearance="fill" class="example-full-width">
                <input matInput placeholder="Ingrese fecha" [matDatepicker]="picker" formControlName="{attribute[1]}"
                [max]="max{attribute[1]}"/>
                <mat-hint>MM/DD/YYYY</mat-hint>
                <mat-datepicker-toggle matIconSuffix [for]="picker"></mat-datepicker-toggle>
                <mat-datepicker #picker></mat-datepicker>
                <mat-error *ngIf="obtenerControlCampo('{attribute[1]}')?.errors?.['required']">
                    {attribute[1]} es obligatorio.
                </mat-error>
            </mat-form-field>
            <br />
            """
        elif attribute[0].lower() not in ['string', 'int', 'double', 'localdate', 'boolean']:
            content += f"""
            <!-- NOTE: Only components with foreign key-->
            <mat-form-field class="example-full-width">
                <mat-label>{attribute[1]}</mat-label>
                <mat-select formControlName="{attribute[1]}">
                    <mat-option *ngFor="let tipo of lista{attribute[0]}" [value]="tipo.id{attribute[0]}">
                        {{{{tipo.id{attribute[0]}}}}}
                    </mat-option>
                </mat-select>
                <mat-error *ngIf="obtenerControlCampo('{attribute[1]}')?.errors?.['required']">
                    {attribute[1]} es obligatorio.
                </mat-error>
            </mat-form-field>
            <br />
            """
    content += f"""
    <!-- Buttons for actions -->
    <button mat-raised-button color="primary">Aceptar</button>
    <button mat-raised-button color="warn" routerLink="/components/{entity["entityName"].lower()}">Cancelar</button>
    <p>{{{{ mensaje }}}}</p>
    </form>
    """

    # Create a folder called ProjectName/src/app/components/entityName/creaedita-entityName
    route = f"{projectName}/src/app/components/{entity['entityName'].lower()}/creaedita-{entity['entityName'].lower()}"
    fileName = f"creaedita-{entity['entityName'].lower()}.component.html"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a html file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate app routing module
def generateAppRoutingModule(projectName):
    content="""
    import { NgModule } from '@angular/core';
    import { RouterModule, Routes } from '@angular/router';
    import { LoginComponent } from './components/login/login.component';

    const routes: Routes = [
    {
        path: '',
        redirectTo: 'login', pathMatch: 'full'
    },
    {
        path: 'login', component: LoginComponent
    },
    {
        path: 'components',
        loadChildren: () => import('./components/components.module').then((m) => m.ComponentsModule),
    }
    ];

    @NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
    })
    export class AppRoutingModule { }
    """

    # Create a folder called ProjectName/src/app
    route = f"{projectName}/src/app"
    fileName = "app-routing.module.ts"
    if not os.path.exists(route):
        os.makedirs(route)
        
    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# generate components routing module
def generateComponentsRoutingModule(projectName, entities):
    """
    import { NgModule } from '@angular/core';
    import { RouterModule, Routes } from '@angular/router';
    import { entityNameComponent } from './entityname/entityname.component';
    import { CreaeditaentityNameComponent } from './entityname/creaedita-entityname/creaedita-entityname.component';

    const routes: Routes = [
    {
        path: 'entityname',
        component: entityNameComponent,
        children: [
        { path: 'nuevo', component: CreaeditaentityNameComponent },
        { path: 'ediciones/:id', component: CreaeditaentityNameComponent }
        ],
    },
    {
        path: 'entityname',
        component: entityNameComponent,
        children: [
        { path: 'nuevo', component: CreaeditaentityNameComponent },
        { path: 'ediciones/:id', component: CreaeditaentityNameComponent }
        ],
    },
    ];

    @NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule],
    })
    export class ComponentsRoutingModule {}
    """

    content = """
    import { NgModule } from '@angular/core';
    import { RouterModule, Routes } from '@angular/router';
    """

    # For each entity
    for entity in entities:
        content += f"import {{ {entity['entityName']}Component }} from './{entity['entityName'].lower()}/{entity['entityName'].lower()}.component';\n"
        content += f"import {{ Creaedita{entity['entityName']}Component }} from './{entity['entityName'].lower()}/creaedita-{entity['entityName'].lower()}/creaedita-{entity['entityName'].lower()}.component';\n"

    content += """
    const routes: Routes = [
    """

    # For each entity
    for entity in entities:
        content += f"""
        {{
            path: '{entity['entityName'].lower()}',
            component: {entity['entityName']}Component,
            children: [
            {{ path: 'nuevo', component: Creaedita{entity['entityName']}Component }},
            {{ path: 'ediciones/:id', component: Creaedita{entity['entityName']}Component }}
            ],
        }},
        """

    content += """
    ];

    @NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule],
    })
    export class ComponentsRoutingModule {}
    """

    # Create a folder called ProjectName/src/app/components
    route = f"{projectName}/src/app/components"
    fileName = "components-routing.module.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate login service
def generateLoginService(projectName):
    content="""
    import { JwtHelperService } from '@auth0/angular-jwt';
    import { HttpClient } from '@angular/common/http';
    import { Injectable } from '@angular/core';
    import { JwtRequest } from '../models/jwtRequest';

    @Injectable({
    providedIn: 'root'
    })
    export class LoginService {

    constructor(private http: HttpClient) { }

    login(request: JwtRequest) {
        return this.http.post("http://localhost:8080/authenticate", request);
    }
    verificar() {
        let token = sessionStorage.getItem("token");
        return token != null;

    }
    showRole(){
        let token = sessionStorage.getItem("token");
        if (!token) {
        // Manejar el caso en el que el token es nulo.
        return null; // O cualquier otro valor predeterminado dependiendo del contexto.
        }
        const helper = new JwtHelperService();
        const decodedToken = helper.decodeToken(token);
        return decodedToken?.role;
    }
    }
    """

    # Create a folder called ProjectName/src/app/services
    route = f"{projectName}/src/app/services"
    fileName = "login.service.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate login component
def generateLoginComponent(projectName):
    content = """
    import { Component, OnInit } from '@angular/core';
    import { Router } from '@angular/router';
    import { JwtRequest } from 'src/app/models/jwtRequest';
    import { LoginService } from 'src/app/services/login.service';
    import { MatSnackBar } from '@angular/material/snack-bar';

    @Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.css']
    })
    export class LoginComponent implements OnInit{
    constructor(private loginService: LoginService, private router: Router, private snackBar: MatSnackBar) { }
    username: string = ""
    password: string = ""
    role: string = ""
    mensaje: string = ""
    ngOnInit(): void {

    }

    login() {
        let request = new JwtRequest();
        request.username = this.username;
        request.password = this.password;
        this.loginService.login(request).subscribe((data: any) => {
        sessionStorage.setItem("token", data.jwttoken);
        if (this.loginService.showRole() == 'ADMIN') {
            this.router.navigate(['components']);
        }
        else if (this.loginService.showRole() == 'USER') {
            this.router.navigate(['components']);
        }
        }, error => {
        this.mensaje = "Credenciales incorrectas!!!"
        this.snackBar.open(this.mensaje, "Aviso",{duration:2000});
        });
    }
    }
    """

    # Create a folder called ProjectName/src/app/components
    route = f"{projectName}/src/app/components/login"
    fileName = "login.component.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate login html
def generateLoginHtml(projectName):
    content = """
    <div>
    <img src="../assets/logoipsum-226.svg" alt="Logo de la empresa" >
    </div>
    <h2>Inicie sesión</h2>
    <mat-form-field class="example-full-width">
    <mat-label>Usuario</mat-label>
    <input matInput placeholder="Username" [(ngModel)]="username" />
    </mat-form-field>
    <br />
    <mat-form-field class="example-full-width">
    <mat-label>Password</mat-label>
    <input
        type="password"
        matInput
        placeholder="Password"
        [(ngModel)]="password"
    />
    </mat-form-field>
    <br />
    <button mat-raised-button color="primary" (click)="login()">Ingresar</button>
    """

    # Create a folder called ProjectName/src/app/components
    route = f"{projectName}/src/app/components/login"
    fileName = "login.component.html"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a html file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate app component Typescript file
def generateAppComponentTypescript(projectName):
    content="""
    import { Component } from '@angular/core';
    import { LoginService } from './services/login.service';

    @Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
    })
    export class AppComponent {
    role:string="";

    constructor(private loginService: LoginService) {
    }
    
    cerrar() {
        sessionStorage.clear();
    }
    verificar() {
        this.role=this.loginService.showRole();
        return this.loginService.verificar();
    }
    validarRol(){
        if(this.role=='ADMIN' || this.role=='USER'){
        return true;
        }else{
        return false;
        }
    }
    }
    """

    # Create a folder called ProjectName/src/app
    route = f"{projectName}/src/app"
    fileName = "app.component.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# Generate app component html file
def generateAppComponentHtml(projectName):
    """
    <mat-toolbar color="primary" *ngIf="verificar()">
    <mat-icon>menu</mat-icon>
    <button mat-button [matMenuTriggerFor]="menuentityName">entityName</button>
    <button mat-button [matMenuTriggerFor]="menuSalir">Usuario</button>
    </mat-toolbar>

    <mat-menu #menuentityName="matMenu">
    <button mat-menu-item routerLink="components/entityname/nuevo">Registrar</button>
    <button mat-menu-item routerLink="components/entityname">Listar</button>
    </mat-menu>

    <mat-menu #menuSalir="matMenu">
    <button mat-menu-item routerLink="/login" (click)="cerrar()">
        <mat-icon>logout</mat-icon>
        <span>Cerrar sesión</span>
    </button>
    <button mat-menu-item>
        Rol: <span>{{role}}</span>
    </button>
    </mat-menu>

    <router-outlet></router-outlet>
    """

    content = """
    <mat-toolbar color="primary" *ngIf="verificar()">
    <mat-icon>menu</mat-icon>
    """

    # For each entity
    for entity in entities:
        content += f"""
        <button mat-button [matMenuTriggerFor]="menu{entity['entityName']}">{entity['entityName']}</button>
        """

    content += """
    <button mat-button [matMenuTriggerFor]="menuSalir">Usuario</button>
    </mat-toolbar>
    """

    # For each entity
    for entity in entities:
        content += f"""
        <mat-menu #menu{entity['entityName']}="matMenu">
        <button mat-menu-item routerLink="components/{entity['entityName'].lower()}/nuevo">Registrar</button>
        <button mat-menu-item routerLink="components/{entity['entityName'].lower()}">Listar</button>
        </mat-menu>
        """

    content += """
    <mat-menu #menuSalir="matMenu">
    <button mat-menu-item routerLink="/login" (click)="cerrar()">
        <mat-icon>logout</mat-icon>
        <span>Cerrar sesión</span>
    </button>
    <button mat-menu-item>
        Rol: <span>{{role}}</span>
    </button>
    </mat-menu>

    <router-outlet></router-outlet>
    """

    # Create a folder called ProjectName/src/app
    route = f"{projectName}/src/app"
    fileName = "app.component.html"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a html file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

def generateProject(fatherDirecory, projectName, entities):
    # Go to the father directory
    os.chdir(fatherDirecory)

    # Execute ng new projectName
    os.system(f"ng new {projectName}")

    # Go to the project directory
    os.chdir(f"{projectName}")
    
    # Print directory
    print("Switched to: ", os.getcwd())

    content = []

    # Install @angular/material
    content.append('ng add @angular/material --legacy-peer-deps')

    # Install moment
    content.append('ng add moment --legacy-peer-deps')

    # Install @auth0/angular-jwt
    content.append('npm install @auth0/angular-jwt --legacy-peer-deps')

    # Install ng2-charts and chart.js
    content.append('npm install ng2-charts chart.js --legacy-peer-deps')

    # npm install
    content.append('npm install --legacy-peer-deps')

    # Commands for generating the entities services, components, creaedita, and listar
    for entity in entities:
        content.append(f'ng g s services/{entity["entityName"].lower()} --skip-tests')
        content.append(f'ng g c components/{entity["entityName"].lower()} --skip-tests')
        content.append(f'ng g c components/{entity["entityName"].lower()}/creaedita-{entity["entityName"].lower()} --skip-tests')
        content.append(f'ng g c components/{entity["entityName"].lower()}/listar-{entity["entityName"].lower()} --skip-tests')
    
    # Generate login component
    content.append('ng g c components/login --skip-tests')

    # Open console and run the commands
    for command in content:
        os.system(command)

    # Return to the father directory
    os.chdir(fatherDirecory)

    # Save the commands in a txt file
    # Create a folder called ProjectName
    route = f"{projectName}"
    fileName = "commands.txt"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a txt file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write('\n'.join(content))
    f.close()

# Generate jwtRequest model
def generateJwtRequestModel(projectName):
    content = """
    export class JwtRequest {
    username: string = "";
    password: string = "";
    }
    """

    # Create a folder called ProjectName/src/app/models
    route = f"{projectName}/src/app/models"
    fileName = "jwtRequest.ts"
    if not os.path.exists(route):
        os.makedirs(route)

    # Create a ts file, write the data and close it
    f = open(f"{route}/{fileName}", "w")
    f.write(content)
    f.close()

# =====================================================================================
# Test the functions

generateProject(fatherDirectory, projectName, entities)
generateEnvironment(projectName)
generateAppModule(projectName)
generateComponentsModule(projectName, entities)
for entity in entities:
    generateEntityModel(projectName, entity)
    generateEntityService(projectName, entity)
    generateEntityComponentTypescript(projectName, entity)
    generateEntityComponentHtmlFile(projectName, entity)
    generateListarEntityTypescript(projectName, entity)
    generateListarEntityHtml(projectName, entity)
    generateEntityComponentCreaEditaTypescriptFile(projectName, entity)
    generateEntityComponentCreaEditaHtmlFile(projectName, entity)
generateAppRoutingModule(projectName)
generateComponentsRoutingModule(projectName, entities)
generateLoginService(projectName)
generateLoginComponent(projectName)
generateLoginHtml(projectName)
generateAppComponentTypescript(projectName)
generateAppComponentHtml(projectName)
generateJwtRequestModel(projectName)
