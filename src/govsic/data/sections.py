from dataclasses import dataclass
from enum import Enum


@dataclass
class Section:
    domain: tuple[int, int]
    description: str
    long_description: str


class Sections(Enum):
    """
    Lookup table for SIC Sections, complete with domains and descriptions.
    """
    A = Section(
        domain = (1000, 4999),
        description = "Agriculture, forestry and fishing",
        long_description = """
            This section includes the exploitation of vegetable and animal natural resources, comprising the activities of growing crops, raising and breeding animals, harvesting timber and other plants, animals or animal products from a farm or their natural habitats.
        """
    )
    B = Section(
        domain = (5000, 9999),
        description = "Mining and quarrying",
        long_description = """
            Mining and quarrying include the extraction of minerals occurring naturally as solids (coal and ores), liquids (petroleum) or gases (natural gas). Extraction can be achieved by different methods such as underground or surface mining, well operation, seabed mining etc.
            This section includes supplementary activities aimed at preparing the crude materials for marketing, for example, crushing, grinding, cleaning, drying, sorting, concentrating ores, liquefaction of natural gas and agglomeration of solid fuels. These operations are often accomplished by the units that extracted the resource and/or others located nearby.
            Mining activities are classified into divisions, groups and classes on the basis of the principal mineral produced. Divisions 05, 06 are concerned with mining and quarrying of fossil fuels (coal, lignite, petroleum, gas); divisions 07, 08 concern metal ores, various minerals and quarry products.
            Some of the technical operations of this section, particularly related to the extraction of hydrocarbons, may also be carried out for third parties by specialised units as an industrial service which is reflected in division 09.
        """
    )
    C = Section(
        domain = (10000, 34999),
        description = "Manufacturing",
        long_description = """
            This section includes the physical or chemical transformation of materials, substances, or components into new products, although this cannot be used as the single universal criterion for defining manufacturing (see remark on processing of waste below). The materials, substances, or components transformed are raw materials that are products of agriculture, forestry, fishing, mining or quarrying as well as products of other manufacturing activities. Substantial alteration, renovation or reconstruction of goods is generally considered to be manufacturing.
            The output of a manufacturing process may be finished in the sense that it is ready for utilisation or consumption, or it may be semi-finished in the sense that it is to become an input for further manufacturing. For example, the output of alumina refining is the input used in the primary production of aluminium; primary aluminium is the input to aluminium wire drawing; and aluminium wire is the input for the manufacture of fabricated wire products.
            Manufacture of specialised components and parts of, and accessories and attachments to, machinery and equipment is, as a general rule, classified in the same class as the manufacture of the machinery and equipment for which the parts and accessories are intended. Manufacture of unspecialised components and parts of machinery and equipment, e.g. engines, pistons, electric motors, electrical assemblies, valves, gears, roller bearings, is classified in the appropriate class of manufacturing, without regard to the machinery and equipment in which these items may be included. However, making specialised components and accessories by moulding or extruding plastics materials is included in group 22.2.
            Assembly of the component parts of manufactured products is considered manufacturing. This includes the assembly of manufactured products from either self-produced or purchased components.
            The recovery of waste, i.e. the processing of waste into secondary raw materials is classified in group 38.3 (Materials recovery). While this may involve physical or chemical transformations, this is not considered to be a part of manufacturing. The primary purpose of these activities is considered to be the treatment or processing of waste and they are therefore classified in Section E (Water supply; sewerage, waste management and remediation activities). However, the manufacture of new final products (as opposed to secondary raw materials) is classified in manufacturing, even if these processes use waste as an input. For example, the production of silver from film waste is considered to be a manufacturing process.
            Specialised maintenance and repair of industrial, commercial and similar machinery and equipment is, in general, classified in division 33 (Repair, maintenance and installation of machinery and equipment). However, the repair of computers and personal and household goods is classified in division 95 (Repair of computers and personal and household goods), while the repair of motor vehicles is classified in division 45 (Wholesale and retail trade and repair of motor vehicles and motorcycles).
            The installation of machinery and equipment, when carried out as a specialised activity, is classified in 33.20.
        """
    )
    D = Section(
        domain = (35000, 35999),
        description = "Electricity, gas, steam and air conditioning supply",
        long_description = """
            This section includes the activity of providing electric power, natural gas, steam, hot water and the like through a permanent infrastructure (network) of lines, mains and pipes. The dimension of the network is not decisive; also included are the distribution of electricity, gas, steam, hot water and the like in industrial parks or residential buildings.
            This section therefore includes the operation of electric and gas utilities, which generate, control and distribute electric power or gas. Also included is the provision of steam and air-conditioning supply.
            This section excludes the operation of water and sewerage utilities, see 36, 37. This section also excludes the (typically long-distance) transport of gas through pipelines.
        """
    )
    E = Section(
        domain = (36000, 40999),
        description = "Water supply; sewerage, waste management and remediation activities",
        long_description = """
            This section includes activities related to the management (including collection, treatment and disposal) of various forms of waste, such as solid or non-solid industrial or household waste, as well as contaminated sites. The output of the waste or sewage treatment process can either be disposed of or become an input into other production processes.
            Activities of water supply are also grouped in this section, since they are often carried out in connection with, or by units also engaged in, the treatment of sewage.
        """
    )
    F = Section(
        domain = (41000, 44999),
        description = "Construction",
        long_description = """
            This section includes general construction and specialised construction activities for buildings and civil engineering works. It includes new work, repair, additions and alterations, the erection of prefabricated buildings or structures on the site and also construction of a temporary nature.
            General construction is the construction of entire dwellings, office buildings, stores and other public and utility buildings, farm buildings etc., or the construction of civil engineering works such as motorways, streets, bridges, tunnels, railways, airfields, harbours and other water projects, irrigation systems, sewerage systems, industrial facilities, pipelines and electric lines, sports facilities etc.
            This work can be carried out on own account or on a fee or contract basis. Portions of the work and sometimes even the whole practical work can be subcontracted out. A unit that carries the overall responsibility for a construction project is classified here.
            Also included is the repair of buildings and civil engineering works.
            This section includes the complete construction of buildings (division 41), the complete construction of civil engineering works (division 42), as well as specialised construction activities, if carried out only as a part of the construction process (division 43).
            The renting of construction equipment with operator is classified with the specific construction activity carried out with this equipment.
            This section also includes the development of building projects for buildings or civil engineering works by bringing together financial, technical and physical means to realise the construction projects for later sale.
            If these activities are carried out not for later sale of the construction projects, but for their operation (e.g. renting of space in these buildings, manufacturing activities in these plants), the unit would not be classified here, but according to its operational activity, i.e. real estate, manufacturing etc.
        """
    )
    G = Section(
        domain = (45000, 48999),
        description = "Wholesale and retail trade; repair of motor vehicles and motorcycles",
        long_description = """
            This section includes wholesale and retail sale (i.e. sale without transformation) of any type of goods, and the supply of services incidental to the sale of merchandise. Wholesaling and retailing are the final steps in the distribution of merchandise. Also included in this section are the repair of motor vehicles and motorcycles.
            Sale without transformation is considered to include the usual operations (or manipulations) associated with trade, for example sorting, grading and assembling of goods, mixing (blending) of goods (for example sand), bottling (with or without preceding bottle cleaning), packing, breaking bulk and repacking for distribution in smaller lots, storage (whether or not frozen or chilled).
            Division 45 includes all activities related to the sale and repair of motor vehicles and motorcycles, while divisions 46 and 47 include all other sale activities. The distinction between division 46 (wholesale) and division 47 (retail sale) is based on the predominant type of customer.
            Wholesale is the resale (sale without transformation) of new and used goods to retailers, business to business trade such as to industrial, commercial, institutional or professional users, or resale to other wholesalers, or involves acting as an agent or broker in buying merchandise for, or selling merchandise to, such persons or companies. The principal types of businesses included are merchant wholesalers, i.e. wholesalers who take title to the goods they sell, such as wholesale merchants or jobbers, industrial distributors, exporters, importers, and cooperative buying associations, sales branches and sales offices (but not retail stores) that are maintained by manufacturing or mining units apart from their plants or mines for the purpose of marketing their products and that do not merely take orders to be filled by direct shipments from the plants or mines. Also included are merchandise and commodity brokers, commission merchants and agents and assemblers, buyers and cooperative associations engaged in the marketing of farm products.
            Wholesalers frequently physically assemble, sort and grade goods in large lots, break bulk, repack and redistribute in smaller lots, for example pharmaceuticals; store, refrigerate, deliver and install goods, engage in sales promotion for their customers and label design.
            Retailing is the resale (sale without transformation) of new and used goods mainly to the general public for personal or household consumption or utilisation, by shops, department stores, stalls, mail-order houses, door-to-door sales persons, hawkers, consumer cooperatives, auction houses etc. Most retailers take title to the goods they sell, but some act as agents for a principal and sell either on consignment or on a commission basis.
        """
    )
    H = Section(
        domain = (49000, 54999),
        description = "Transportation and storage",
        long_description = """
            This section includes the provision of passenger or freight transport, whether scheduled or not, by rail, pipeline, road, water or air and associated activities such as terminal and parking facilities, cargo handling, storage etc. Included in this section is the renting of transport equipment with driver or operator. Also included are postal and courier activities.
            This section excludes:
                - major repair or alteration of transport equipment, except motor vehicles, see group 33.1
                - construction, maintenance and repair of roads, railways, harbours, airfields, see division 42
                - maintenance and repair of motor vehicles, see 45.20
                - renting of transport equipment without driver or operator, see 77.1, 77.3
        """
    )
    I = Section(
        domain = (55000, 57999),
        description = "Accommodation and food service activities",
        long_description = """
            This section includes the provision of short-stay accommodation for visitors and other travellers and the provision of complete meals and drinks fit for immediate consumption. The amount and type of supplementary services provided within this section can vary widely.
            This section excludes the provision of long-term accommodation as primary residences, which is classified in real estate activities (section L). Also excluded is the preparation of food or drinks that are either not fit for immediate consumption or that are sold through independent distribution channels, i.e. through wholesale or retail trade activities. The preparation of these foods is classified in manufacturing (section C).
        """
    )
    J = Section(
        domain = (58000, 63999),
        description = "Information and communication",
        long_description = """
            This section includes the production and distribution of information and cultural products, the provision of the means to transmit or distribute these products, as well as data or communications, information technology activities and the processing of data and other information service activities.
            The main components of this section are publishing activities (division 58), including software publishing, motion picture and sound recording activities (division 59), radio and TV broadcasting and programming activities (division 60), telecommunications activities (division 61), information technology activities (division 62) and other information service activities (division 63).
            Publishing includes the acquisition of copyrights for content (information products) and making this content available to the general public by engaging in (or arranging for) the reproduction and distribution of this content in various forms. All the feasible forms of publishing (in print, electronic or audio form, on the internet, as multimedia products such as CD-ROM reference books etc.) are included in this section.
            Activities related to production and distribution of TV programming span divisions 59, 60 and 61, reflecting different stages in this process. Individual components, such as movies, television series etc. are produced by activities in division 59, while the creation of a complete television channel programme, from components produced in division 59 or other components (such as live news programming) is included in division 60. Division 60 also includes the broadcasting of this programme by the producer. The distribution of the complete television programme by third parties, i.e. without any alteration of the content, is included in division 61. This distribution in division 61 can be done through broadcasting, satellite or cable systems.
        """
    )
    K = Section(
        domain = (64000, 67999),
        description = "Financial and insurance activities",
        long_description = """
            This section includes financial service activities, including insurance, reinsurance and pension funding activities, and activities to support financial services.
            This section also includes the activities of holding assets, such as activities of holding companies and the activities of trusts, funds and similar financial entities.
        """
    )
    L = Section(
        domain = (68000, 68999),
        description = "Real estate activities",
        long_description = """
            This section includes acting as lessors, agents and/or brokers in one or more of the following: selling or buying real estate, renting real estate, providing other real estate services such as appraising real estate or acting as real estate escrow agents. Activities in this section may be carried out on own or leased property and may be done on a fee or contract basis.
            Also included is the building of structures, combined with maintaining ownership or leasing of such structures.
            This section includes real estate property managers.
        """
    )
    M = Section(
        domain = (69000, 76999),
        description = "Professional, scientific and technical activities",
        long_description = """
            This section includes specialised professional, scientific and technical activities. These activities require a high degree of training, and make specialised knowledge and skills available to users.
        """
    )
    N = Section(
        domain = (77000, 83999),
        description = "Administrative and support service activities",
        long_description = """
            This section includes a variety of activities that support general business operations. These activities differ from those in section M, in that their primary purpose is not the transfer of specialised knowledge.
        """
    )
    O = Section(
        domain = (84000, 84999),
        description = "Public administration and defence; compulsory social security",
        long_description = """
            This section includes activities of a governmental nature, normally carried out by the public administration. This includes the enactment and judicial interpretation of laws and their pursuant regulation, as well as the administration of programmes based on them, legislative activities, taxation, national defence, public order and safety, immigration services, foreign affairs and the administration of government programmes.
            This section also includes compulsory social security activities.
            The legal or institutional status is not, in itself, the determining factor for an activity to belong in this section, rather than the activity being of a nature specified in the previous paragraph. This means that activities classified elsewhere in SIC do not fall under this section, even if carried out by public entities. For example, administration of the school system (i.e. regulations, checks, curricula) falls under this section, but teaching itself does not (see section P), and a prison or military hospital is classified to health (see section Q). Similarly, some activities described in this section may be carried out by non-government units.
        """
    )
    P = Section(
        domain = (85000, 85999),
        description = "Education",
        long_description = """
            This section includes education at any level or for any profession. The instruction may be oral or written and may be providedbby radio, television, Internet or via correspondence.
            It includes education by the various institutions in the regular school system at its different levels as well as adult education, literacy programmes etc. Also included are military schools and academies, prison schools etc. at their respective levels. The section includes public as well as private education.
            For each level of initial education, the classes include special education for physically or mentally disabled pupils.
            The breakdown of the categories in this section is based on the level of education offered as defined by the levels of ISCED 1997. The activities of educational institutions providing courses on ISCED level 0 are classified in 85.10, on ISCED level 1 in 85.20, on ISCED levels 2-3 in group 85.3, on ISCED level 4 in 85.41 and on ISCED level 5-6 in 85.42.
            This section also includes instruction primarily concerned with sport and recreational activities such as tennis or golf and education support activities.
        """
    )
    Q = Section(
        domain = (86000, 89999),
        description = "Human health and social work activities",
        long_description = """
            This section includes the provision of health and social work activities. It covers a wide range of activities, from health care provided by trained medical professionals in hospitals and other facilities, to residential care activities that still involve a degree of health care activities and to social work activities not involving the services of health care professionals.
        """
    )
    R = Section(
        domain = (90000, 93999),
        description = "Arts, entertainment and recreation",
        long_description = """
            This section includes a wide range of activities catering for various cultural, entertainment and recreational interests of the general public, including live performances, operation of museum sites, gambling, sports and recreation activities.
        """
    )
    S = Section(
        domain = (94000, 96999),
        description = "Other service activities",
        long_description = """
            This section (as a residual category) includes the activities of membership organisations, the repair of computers and personal and household goods and a variety of personal service activities not covered elsewhere in the classification.
        """
    )
    T = Section(
        domain = (97000, 98999),
        description = "Activities of households as employers; undifferentiated goods- and services-producing activities of households for own use",
        long_description = """
            Activities of households as employers of domestic personnel.
        """
    )
    U = Section(
        domain = (99000, 99999),
        description = "Activities of extraterritorial organisations and bodies",
        long_description = """
            This class includes:
                - activities of international organisations such as the United Nations and the specialised agencies of the United Nations system,– regional bodies etc., the International monetary Fund, the World Bank, the World Customs Organisation, the Organisation for Economic Co-operation and Development, the Organisation of Petroleum Exporting Countries, the European Communities, the European Free Trade Association etc.
            This class also includes:
                - activities of diplomatic and consular missions when being determined by the country of their location rather than by the– country they represent
        """
    )
