from classes import *

# Setando os mocks dos eventos
evento1 = Evento(
    1,
    'Maratona de Programação 2024.2',
    'Prepare-se para desafiar suas habilidades de programação na Maratona de Programação 2024.2, liderada por Tassio Auad, um renomado especialista em algoritmos e competições de programação. Neste evento emocionante, você terá a oportunidade de testar seu conhecimento em algoritmos, resolver problemas complexos e trabalhar em equipe para encontrar soluções eficientes. O evento será realizado no Laboratório de Informática 4, um ambiente propício para estimular sua criatividade e concentração. Não perca a chance de competir com os melhores programadores, aprimorar suas habilidades e quem sabe até conquistar um lugar no pódio! Venha fazer parte desta emocionante jornada rumo à excelência em programação.',
    'Tassio Auad',
    'Laboratório de Informática 4 - Bloco 9 - Univassouras',
    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2011.179640351281!2d-43.664727955834714!3d-22.40945903987602!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9930cf7c22de05%3A0xc63f64f24c89cbf6!2sUniversidade%20de%20Vassouras!5e0!3m2!1spt-BR!2sbr!4v1716749106718!5m2!1spt-BR!2sbr',
    'img/maratona-programacao.png',
    '01',
    'JUNHO'
)

evento2 = Evento(
    2,
    'Workshop de Desenvolvimento Ágil',
    'Venha participar do nosso Workshop de Desenvolvimento Ágil, liderado por Lucas Oliveira, um especialista em metodologias ágeis. Neste workshop, você aprenderá sobre os princípios fundamentais do desenvolvimento ágil de software, incluindo Scrum, Kanban e Lean. Descubra como implementar práticas ágeis em sua equipe de desenvolvimento e leve seus projetos ao próximo nível de eficiência e qualidade. Não perca esta oportunidade de se tornar um profissional mais ágil e adaptável em um mercado de tecnologia em constante evolução.',
    'Caio Jannuzzi',
    'Laboratório de Informática 2 - Bloco 9 - Univassouras',
    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2011.179640351281!2d-43.664727955834714!3d-22.40945903987602!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9930cf7c22de05%3A0xc63f64f24c89cbf6!2sUniversidade%20de%20Vassouras!5e0!3m2!1spt-BR!2sbr!4v1716749106718!5m2!1spt-BR!2sbr',
    'img/workshop-agil.png',
    '15',
    'JULHO'
)

evento3 = Evento(
    3,
    'Palestra sobre DevOps: Cultura, Práticas e Ferramentas',
    'Participe da nossa Palestra sobre DevOps, ministrada por Ana Souza, uma referência na integração entre desenvolvimento e operações. Nesta palestra envolvente, você explorará a cultura, as práticas e as ferramentas essenciais do movimento DevOps. Aprenda como superar as barreiras entre equipes de desenvolvimento e operações, acelerar a entrega de software e melhorar a qualidade do produto final. Junte-se a nós para uma jornada de descoberta e transformação no universo do DevOps.',
    'Carlos Vitor',
    'Auditório Principal - Bloco 9 - Univassouras',
    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2011.179640351281!2d-43.664727955834714!3d-22.40945903987602!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9930cf7c22de05%3A0xc63f64f24c89cbf6!2sUniversidade%20de%20Vassouras!5e0!3m2!1spt-BR!2sbr!4v1716749106718!5m2!1spt-BR!2sbr',
    'img/palestra-devops.png',
    '10',
    'AGOSTO'
)

eventosMocks = [evento1, evento2, evento3]

# Setando os mocks das instalações
instalacao1 = Instalacao(
    1,
    'Biblioteca Central',
    'A Biblioteca Central oferece um vasto acervo de livros, periódicos e recursos digitais, proporcionando um ambiente propício para estudos e pesquisas.',
    'Bloco 2 - Univassouras',
    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2011.179640351281!2d-43.664727955834714!3d-22.40945903987602!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9930cf7c22de05%3A0xc63f64f24c89cbf6!2sUniversidade%20de%20Vassouras!5e0!3m2!1spt-BR!2sbr!4v1716749106718!5m2!1spt-BR!2sbr',
    'img/biblioteca-univassouras.png',
    'Seg-Sex: 8h - 22h, Sáb: 8h - 14h',
    15,
    '(24) 2471-8200'
)

instalacao2 = Instalacao(
    2,
    'Laboratório de Informática',
    'Equipado com computadores modernos e softwares atualizados, o Laboratório de Informática está disponível para aulas práticas e estudos individuais.',
    'Bloco 3 - Univassouras',
    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2011.179640351281!2d-43.664727955834714!3d-22.40945903987602!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9930cf7c22de05%3A0xc63f64f24c89cbf6!2sUniversidade%20de%20Vassouras!5e0!3m2!1spt-BR!2sbr!4v1716749106718!5m2!1spt-BR!2sbr',
    'img/lab-informatica-univassouras.png',
    'Seg-Sex: 8h - 18h',
    3,
    '(24) 2471-8201'
)

instalacao3 = Instalacao(
    3,
    'Área de Lazer',
    'A Área de Lazer oferece um espaço para descanso e socialização, com jardins, bancos e uma quadra de esportes.',
    'Bloco 1 - Univassouras',
    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2011.179640351281!2d-43.664727955834714!3d-22.40945903987602!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9930cf7c22de05%3A0xc63f64f24c89cbf6!2sUniversidade%20de%20Vassouras!5e0!3m2!1spt-BR!2sbr!4v1716749106718!5m2!1spt-BR!2sbr',
    'img/area-lazer-univassouras.png',
    'Todos os dias: 6h - 22h',
    25,
    '(24) 2471-8202'
)

instalacoesMocks = [instalacao1, instalacao2, instalacao3]