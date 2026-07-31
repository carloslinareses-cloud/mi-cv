# -*- coding: utf-8 -*-
"""
Los cuatro perfiles. Mismo historial laboral real, contado con el vocabulario
que espera cada tipo de oferta.

TODO sale del CV publicado en https://carloslinareses-cloud.github.io/mi-cv/
Puestos, empresas y fechas son los reales y no se tocan. Lo único que cambia
entre versiones es qué puestos se detallan y qué se destaca de cada uno.

Reglas aprendidas revisando la primera versión, que tenía errores de bulto:
  - Nada de herramientas que no estén respaldadas por un puesto concreto. Pasan
    el filtro automático y revientan en la primera pregunta ("¿con qué CRM?").
  - Nada que se contradiga con otra línea del mismo documento.
  - El cargo de cada puesto es EXACTAMENTE el del CV publicado: la web y
    LinkedIn se comprueban con los enlaces que el propio CV ofrece.
"""

# --- historial laboral real --------------------------------------------------
# 'desde' solo sirve para ordenar. 'fechas' es lo que se imprime, en MM/AAAA.

ALCALDIA = {
    "desde": "2026-04",
    "puesto": "Desarrollador de Software",
    "empresa": "Alcaldía de Charallave",
    "lugar": "Miranda, Venezuela",
    "fechas": "04/2026 – Presente",
    "logros": [
        "App Android de asistencia y control de acceso para más de 255 empleados, que redujo cerca del 90% el tiempo de marcaje: Kotlin y Jetpack Compose, biometría, PIN cifrado AES-256-GCM, geocercas y actualización remota.",
        "Panel administrativo y backend con React 19 y Supabase/PostgreSQL: 18 tablas y 3 Edge Functions, gestión de más de 255 carnets y más de 30 informes en PDF y Excel.",
        "Integración de consulta de cédula ante el CNE.",
    ],
}

ALCALDIA_SOPORTE = dict(ALCALDIA, logros=[
    "Desarrollo y soporte de sistemas internos para más de 255 empleados: despliegue de la aplicación, actualización remota del parque de dispositivos, resolución de incidencias de acceso y generación de más de 30 informes operativos.",
])

# El cargo es el del CV publicado. El enfoque a operaciones se consigue en las
# viñetas, nunca cambiando el título: eso crearía una discrepancia con la web.
PANAVOY = {
    "desde": "2026-02",
    "puesto": "Fundador y Desarrollador Full-Stack",
    "empresa": "Pana Voy",
    "lugar": "Venezuela · Proyecto propio",
    "fechas": "02/2026 – Presente",
    "logros": [
        "App Android multi-rol publicada en Google Play: unas 43.000 líneas de Kotlin y 248 componentes Compose, con MapLibre, geocercas y GPS en tiempo real, operando más de 300 entregas al mes.",
        "Backend sin servidor con 35 Firebase Cloud Functions (Node 20) y 4 Cloudflare Workers, con observabilidad y alertas, disponibilidad cercana al 99,9%.",
        "Migración de Google Maps a MapLibre y retirada del SDK de AWS: 25 MB menos de aplicación.",
    ],
}

PANAVOY_ATENCION = dict(PANAVOY, logros=[
    "Como fundador asumo también la operación diaria: atención a clientes, comercios y repartidores por chat y WhatsApp, como único punto de contacto de la plataforma y con responsabilidad de cierre de cada caso.",
    "Gestión de reclamaciones e incidencias de pedidos, cobros y entregas, con seguimiento hasta resolverlas.",
    "Alta y verificación de comercios y repartidores; liquidaciones y cuadre de pagos a socios.",
])

PARKMADRID = {
    "desde": "2023-07",
    "puesto": "Gerente, Administrador y Operador Logístico",
    "empresa": "ParkMadrid",
    "lugar": "Madrid, España",
    "fechas": "07/2023 – 01/2026",
    "logros": [
        "Coordinación de personal y organización de los turnos de trabajo.",
        "Resolución de incidencias operativas del día a día y seguimiento de procesos.",
        "Control de inventarios, documentación administrativa y elaboración de informes.",
    ],
}

OURWORLD = {
    "desde": "2023-03",
    "puesto": "Backend Junior",
    "empresa": "Ourworld LTD",
    "lugar": "Madrid, España",
    "fechas": "03/2023 – 05/2023",
    "logros": [
        "Desarrollo en Python y creación de APIs REST con Flask; operaciones CRUD y scripts a medida.",
    ],
}

WIFITEL = {
    "desde": "2021-11",
    "puesto": "Soporte Técnico",
    "empresa": "WIFITEL",
    "lugar": "Cúa, Venezuela",
    "fechas": "11/2021 – 02/2022",
    "logros": [
        "Instalación y mantenimiento de servicios de internet en casa del cliente, con atención directa al usuario.",
        "Configuración de antenas Ubiquiti y redes inalámbricas; administración de routers.",
        "Cableado estructurado RJ45.",
    ],
}

COFESCO = {
    "desde": "2020-11",
    "puesto": "Notificador",
    "empresa": "COFESCO",
    "lugar": "Bogotá, Colombia",
    "fechas": "11/2020 – 07/2021",
    "logros": [
        "Registro y validación de documentación de predios y actualización de bases de datos.",
    ],
}

TELEPERFORMANCE = {
    "desde": "2020-07",
    "puesto": "Agente de Contact Center",
    "empresa": "Teleperformance",
    "lugar": "Bogotá, Colombia",
    "fechas": "07/2020 – 11/2020",
    "logros": [
        "Atención al cliente y soporte técnico de primer nivel en campaña de contact center.",
        "Escalamiento de incidencias a segundo nivel siguiendo los protocolos establecidos.",
        "Gestión de backoffice y registro de cada caso en el sistema.",
    ],
}

FLOTAS = {
    "desde": "2018-11",
    "puesto": "Jefe de Servicio y Analista Post Venta",
    "empresa": "Flotas Service SPA",
    "lugar": "Santiago, Chile",
    "fechas": "11/2018 – 07/2019",
    "logros": [
        "Elaboración de presupuestos, gestión de repuestos y tarifarios, y control de mantenimiento de flotas, con manejo de bases de datos y Excel avanzado.",
    ],
}

NOVATEX = {
    "desde": "2016-06",
    "puesto": "Operador Informático",
    "empresa": "Inversiones Novatex",
    "lugar": "Bogotá, Colombia",
    "fechas": "06/2016 – 05/2018",
    "logros": [
        "Mantenimiento de servidores y equipos; instalación de redes y CCTV; configuración de routers.",
        "Atención al cliente y manejo de personal.",
    ],
}

BODEGON = {
    "desde": "2010-03",
    "puesto": "Gerente de Ventas",
    "empresa": "Bodegón Chara",
    "lugar": "Charallave, Venezuela",
    "fechas": "03/2010 – 12/2015",
    "logros": [
        "Gestión de ventas y atención al cliente; soporte técnico de hardware y software; administración de redes y CCTV.",
    ],
}

# El candidato confirmó: inglés SOLO de lectura. "A nivel profesional" es
# terminología de escala que un reclutador lee como "puede trabajar en inglés",
# y si el filtro telefónico es en inglés se cae la candidatura.
IDIOMAS = ("Español: nativo. Inglés: lectura y comprensión escrita "
           "(documentación técnica, correo y tickets). No conversacional.")

ADICIONAL_BASE = [
    "Disponibilidad: incorporación inmediata, jornada completa.",
    "Trabajo 100% remoto, con disponibilidad para turnos rotativos, turnos nocturnos y fines de semana.",
    "Zona horaria GMT-4 (Venezuela): jornada completa coincidente con EE. UU. y Latinoamérica, y solapamiento con la tarde en España.",
    "Equipo propio: portátil, auriculares con micrófono y conexión a internet estable, en espacio de trabajo sin interrupciones.",
]

# Frase que desactiva la objeción número uno de los perfiles no técnicos: un
# desarrollador en activo pidiendo un puesto de soporte parece que se irá en
# tres meses, y el reclutador resuelve esa duda solo y mal.
NO_ES_ESCALA = (
    " Trabajo desde Venezuela y busco una posición remota estable a jornada completa. "
    "Mi perfil técnico es una ventaja para el puesto, no una escala: aporta diagnóstico "
    "propio, autonomía y automatización de las tareas repetitivas del rol."
)


PERFILES = [
    {
        "archivo": "CV-Carlos-Linares-Desarrollador-ATS.docx",
        "especialidad": "Desarrollador Full Stack",
        "github": True,
        "titular": "Desarrollador Full Stack · Android y Backend · Web y Cloud",
        "resumen": (
            "Desarrollador full stack con 7 productos en producción y 2 aplicaciones Android "
            "nativas, una publicada en Google Play. Especializado en Kotlin y Jetpack Compose, "
            "React y TypeScript, Node.js y bases de datos Supabase, Firebase y PostgreSQL. "
            "Base en soporte técnico, redes e infraestructura desde 2016, primera experiencia "
            "backend profesional en 2023 (Python y Flask, Ourworld LTD) y dedicación completa al "
            "desarrollo de software desde 2026. Entrego de extremo a extremo: arquitectura, APIs "
            "REST, pagos, mapas en tiempo real, pruebas automatizadas y despliegue continuo."
        ),
        "experiencia": [ALCALDIA, PANAVOY, OURWORLD, WIFITEL, NOVATEX],
        "breves": [PARKMADRID, COFESCO, TELEPERFORMANCE, FLOTAS, BODEGON],
        "proyectos": [
            "Pana Voy — delivery y transporte, app Android en Google Play (Kotlin, Compose, MapLibre, Firebase).",
            "Ecosistema digital municipal de Charallave — portal, sala situacional y app de asistencia.",
            "Resuelia — marketplace de servicios en Colombia: React/TypeScript, Supabase con RLS, pagos Wompi.",
            "FUNCECAIND Aula Virtual — LMS con evaluaciones en servidor, certificados con QR y clases en vivo.",
            "AeroSocio — club digital para conductores en España: React 19, Supabase, pagos SumUp.",
            "Eternia — infraestructura de servidores con Docker, Caddy y MariaDB.",
            "Súmate VZLA — recaudación con checkout en varias monedas y pruebas E2E y de accesibilidad.",
        ],
        "habilidades": [
            ("Móvil", ["Kotlin", "Jetpack Compose", "Android Studio", "Capacitor"]),
            ("Frontend", ["React", "TypeScript", "JavaScript", "Astro", "Tailwind CSS", "HTML", "CSS"]),
            ("Backend y datos", ["Node.js", "Python", "Flask", "APIs REST", "PostgreSQL", "SQL/RLS", "Pandas", "Supabase", "Firebase"]),
            ("Cloud y DevOps", ["Cloudflare Workers", "R2 Storage", "Edge Functions", "Docker", "Caddy", "Linux", "Git", "CI/CD"]),
            ("Calidad y pagos", ["Playwright", "Vitest", "JUnit", "SumUp", "Wompi", "OpenAI API"]),
        ],
        "idiomas": IDIOMAS,
        "adicional": ADICIONAL_BASE,
    },
    {
        "archivo": "CV-Carlos-Linares-Soporte-Tecnico-ATS.docx",
        "especialidad": "Soporte Tecnico Remoto",
        "github": True,
        "titular": "Soporte Técnico Remoto · Helpdesk, Redes e Infraestructura",
        "resumen": (
            "Técnico con experiencia en soporte a usuarios, redes e infraestructura desde 2016, "
            "incluida una campaña de contact center con soporte de primer nivel y escalamiento "
            "estructurado a segundo nivel. Acostumbrado a atender incidencias de principio a fin, "
            "documentarlas y explicar la solución a personas sin conocimientos técnicos. Manejo de "
            "Windows y Linux, redes inalámbricas, routers y CCTV, y experiencia en desarrollo de "
            "software desde 2026, que uso para diagnosticar incidencias hasta la causa raíz."
            + NO_ES_ESCALA
        ),
        "experiencia": [WIFITEL, TELEPERFORMANCE, NOVATEX, ALCALDIA_SOPORTE, BODEGON],
        "breves": [PANAVOY_ATENCION, PARKMADRID, OURWORLD, COFESCO, FLOTAS],
        "habilidades": [
            ("Soporte", ["Helpdesk", "Soporte nivel 1 con escalamiento estructurado a nivel 2", "Atención a usuarios", "Diagnóstico de incidencias", "Instalación y mantenimiento en campo", "Registro y seguimiento de casos", "Documentación de incidencias"]),
            ("Sistemas", ["Windows", "Linux", "Microsoft Office", "SAINT", "SIGA", "Mantenimiento de servidores y equipos"]),
            ("Redes", ["TCP/IP", "Routers", "Ubiquiti", "Redes inalámbricas", "Cableado estructurado", "RJ45", "CCTV"]),
            ("Automatización", ["Python", "Docker", "Git"]),
        ],
        "idiomas": IDIOMAS,
        "adicional": ADICIONAL_BASE,
    },
    {
        "archivo": "CV-Carlos-Linares-Atencion-Cliente-ATS.docx",
        "especialidad": "Atencion al Cliente y Contact Center",
        # Sin GitHub: en este perfil es un cartel de "soy programador y esto es
        # temporal", justo el riesgo de fuga que hay que desactivar.
        "github": False,
        "titular": "Atención al Cliente y Contact Center · Remoto",
        "resumen": (
            "Más de 10 años de trato directo con clientes: comercio (2010-2015), soporte "
            "informático (2016-2018), contact center y trabajo de campo (2020-2022) y gestión de "
            "operaciones y equipos (2023-2026), incluida una campaña en Teleperformance Bogotá "
            "(atención, soporte técnico de primer nivel, escalamiento y backoffice). Actualmente "
            "atiendo a diario a clientes, comercios y repartidores en mi propia plataforma. "
            "Perfil técnico: TSU en Informática y experiencia en soporte de redes, equipos y CCTV, "
            "lo que me permite diagnosticar la incidencia antes de escalarla y explicarla con "
            "precisión al segundo nivel." + NO_ES_ESCALA
        ),
        "experiencia": [PANAVOY_ATENCION, PARKMADRID, WIFITEL, TELEPERFORMANCE, NOVATEX, BODEGON],
        "breves": [ALCALDIA_SOPORTE, OURWORLD, COFESCO, FLOTAS],
        "habilidades": [
            ("Atención al cliente", ["Call center", "Contact center", "Servicio al cliente", "Atención al cliente", "Soporte al cliente", "Teleoperador", "Atención telefónica", "Atención por chat", "Gestión de reclamaciones", "Resolución de incidencias", "Escalamiento a segundo nivel", "Backoffice", "Seguimiento de casos"]),
            ("Herramientas", ["Microsoft Office", "Excel", "WhatsApp", "SAINT", "SIGA", "Registro y seguimiento de casos en sistema"]),
            ("Competencias", ["Comunicación clara", "Escucha activa", "Paciencia", "Trabajo por turnos", "Trabajo por objetivos", "Coordinación de equipo"]),
            ("Técnicas", ["Soporte nivel 1", "Windows", "Redes"]),
        ],
        "idiomas": IDIOMAS,
        "adicional": ADICIONAL_BASE,
    },
    {
        "archivo": "CV-Carlos-Linares-Asistente-Virtual-ATS.docx",
        "especialidad": "Asistente Virtual y Soporte Administrativo",
        "github": False,
        "titular": "Asistente Virtual · Soporte Administrativo y Automatización",
        "resumen": (
            "Perfil administrativo con base técnica: dos años y medio como gerente y administrador "
            "en ParkMadrid gestionando documentación, inventarios, turnos e informes, más "
            "experiencia en contact center, en registro y validación documental y en elaboración de "
            "presupuestos con Excel avanzado. Manejo alto de hojas de cálculo y capacidad poco "
            "habitual en el puesto: programo, así que automatizo las tareas repetitivas en vez de "
            "repetirlas." + NO_ES_ESCALA
        ),
        "experiencia": [PANAVOY_ATENCION, PARKMADRID, COFESCO, TELEPERFORMANCE, FLOTAS],
        "breves": [ALCALDIA_SOPORTE, OURWORLD, WIFITEL, NOVATEX, BODEGON],
        "habilidades": [
            ("Administrativas", ["Gestión documental", "Elaboración de informes", "Control de inventarios", "Organización de turnos", "Coordinación de personal", "Entrada de datos", "Presupuestos y facturación"]),
            ("Herramientas", ["Microsoft Office", "Excel avanzado", "Hojas de cálculo", "SAINT", "SIGA"]),
            ("Automatización", ["Python", "Hojas de cálculo automatizadas", "Informes automáticos", "Alertas y observabilidad automatizadas"]),
            ("Competencias", ["Organización", "Autonomía", "Atención al detalle", "Confidencialidad", "Comunicación escrita"]),
        ],
        "idiomas": IDIOMAS,
        "adicional": ADICIONAL_BASE,
    },
]
