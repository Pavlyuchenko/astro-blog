<script>
    import { onMount } from "svelte";

    onMount(() => {
        document
            .getElementById("article")
            .querySelectorAll(".table_of_contents-link")
            .forEach((a) => {
                a.addEventListener("click", (event) => {
                    event.preventDefault();
                    document
                        .getElementById(a.getAttribute("href").replace("#", ""))
                        .scrollIntoView();
                });
            });
    });
</script>

<svelte:head>
    <title>Studium v zahraničí: Jak se dostat na univerzitu v Nizozemsku</title>
    <meta
        name="description"
        content="Zjisti co obnáší studium v zahraničí, na co si dát pozor před odjezdem a na co se psychicky připravit."
    />
    <meta name="robots" content="index, follow" />

    <meta
        property="og:title"
        content="Studium v zahraničí: Jak se dostat na univerzitu v Nizozemsku"
    />
    <meta property="og:type" content="article" />
    <meta
        property="og:url"
        content="https://michal-pavlicek.tech/article/vyplati-se-zahranicni-univerzita"
    />
    <meta property="og:image" content="fb_studium.png" />

    <meta
        name="twitter:title"
        content="Studium v zahraničí: Jak se dostat na univerzitu v Nizozemsku"
    />
    <meta
        name="twitter:description"
        content="Zjisti co obnáší studium v zahraničí, na co si dát pozor před odjezdem a na co se psychicky připravit."
    />
    <meta name="twitter:image" content="fb_studium.png" />
    <meta name="twitter:card" content="summary_large_image" />
</svelte:head>

<h1 id="title">
    Studium v zahraničí: <br />
    Jak se dostat na univerzitu v Nizozemí
</h1>
<div id="article-details">
    <p>Michal Pavlíček</p>
    <span> |</span>
    <p>Studium v zahraničí</p>
    <span> |</span>
    <p>02. 10. 2022</p>
</div>
<section id="article">
    <div>
        <p id="bbd305c8-913b-4fbd-ad90-7983683ea63e" class="first-paragraph">
            Před třemi týdny jsem poprvé ve svém životě vyrazil na vlastní pěst
            do cizí země. Do země, kde jsem nikoho neznal a kde pravděpodobně
            strávím alespoň následující tři roky. Rozhodl jsem se totiž po
            maturitě studovat na univerzitě v Nizozemsku, konkrétně ve městě
            Maastricht. Během příprav na odjezd a samotného odjezdu jsem si
            prošel mnoha různými psychickými stavy od téměř panického strachu,
            smutku, pochyb, až konečně k přijetí svého rozhodnutí a ke
            spokojenosti.
        </p>
        <p id="7039ca68-fc18-454a-896f-2ae8fa7c61ea">
            V průběhu této, prozatím krátké, ale rozhodně ne strohé, cesty jsem
            narazil na několik různých problémů, které jsem při plánování
            neočekával. V následujících kapitolách bych rád předal své
            zkušenosti a vyprávěl svůj příběh, tedy příběh stěhování se z Česka
            do zahraničí. Ať už si teprve pohráváte s myšlenkou studia v
            zahraničí nebo se na něj již připravujete, mým cílem je nastínit, co
            vše takové rozhodnutí obnáší a co je třeba zvážit.
        </p>
        <p id="fdf7dd84-84ff-4423-a98c-dd23e49c1d22">
            <em
                >Jelikož je článek poměrně dlouhý, navrhuji, abyste se zaměřili
                především na části, které vás opravdu zajímají:</em
            >
        </p>
        <nav
            id="779c7a25-6806-4836-92f3-db7dbad6ea69"
            class="block-color-gray table_of_contents"
        >
            <div class="table_of_contents-item table_of_contents-indent-0">
                <a
                    class="table_of_contents-link"
                    href="#735fcb7a-560a-41eb-a432-781047d2f08f"
                    >Plánování studia mimo Česko</a
                >
            </div>
            <div class="table_of_contents-item table_of_contents-indent-1">
                <a
                    class="table_of_contents-link"
                    href="#a8f80ebe-a970-4b8b-a9c9-568aa8176374"
                    >Kde hledat zahraniční univerzity</a
                >
            </div>
            <div class="table_of_contents-item table_of_contents-indent-1">
                <a
                    class="table_of_contents-link"
                    href="#e14969b3-ef26-45fa-8744-03a47171d30d"
                    >Přijímačky na nizozemských univerzitách</a
                >
            </div>
            <div class="table_of_contents-item table_of_contents-indent-1">
                <a
                    class="table_of_contents-link"
                    href="#d4fd899b-6cb4-4013-a35d-176c221bda45"
                    >Hledání studentského ubytování v zahraničí</a
                >
            </div>
            <div class="table_of_contents-item table_of_contents-indent-1">
                <a
                    class="table_of_contents-link"
                    href="#c3e32186-116a-4845-9483-afd8a6265e59"
                    >Úskalí při hledání ubytování</a
                >
            </div>
            <div class="table_of_contents-item table_of_contents-indent-1">
                <a
                    class="table_of_contents-link"
                    href="#1015a6b6-4df7-4ed0-9eba-19e72e932ef4"
                    >Mé zkušenosti s hledáním bytu</a
                >
            </div>
            <div class="table_of_contents-item table_of_contents-indent-1">
                <a
                    class="table_of_contents-link"
                    href="#dd45c0f5-7465-4ea3-a26a-525df63e5c9e"
                    >Co je třeba zařídit před odjezdem na zahraniční univerzitu</a
                >
            </div>
            <div class="table_of_contents-item table_of_contents-indent-0">
                <a
                    class="table_of_contents-link"
                    href="#ffea702d-01d3-4cad-92ee-fc95c1f3192d"
                    >Odjezd do zahraničí</a
                >
            </div>
            <div class="table_of_contents-item table_of_contents-indent-1">
                <a
                    class="table_of_contents-link"
                    href="#2eb72d00-8d7d-442d-8de1-89041bb8fdc3"
                    >Pocity před odjezdem</a
                >
            </div>
            <div class="table_of_contents-item table_of_contents-indent-1">
                <a
                    class="table_of_contents-link"
                    href="#6fb013a0-4f13-4c96-9ce6-ab988d86e0ef"
                    >Seznamovací týden na univerzitě</a
                >
            </div>
            <div class="table_of_contents-item table_of_contents-indent-1">
                <a
                    class="table_of_contents-link"
                    href="#451ff8c2-30d0-4852-8e2a-4049cc1c1cd2"
                    >Hledání kamarádů v zahraničí</a
                >
            </div>
            <div class="table_of_contents-item table_of_contents-indent-0">
                <a
                    class="table_of_contents-link"
                    href="#4033e36a-ba09-407e-bae3-808013c26314"
                    >Studovat na univerzitě v zahraničí?</a
                >
            </div>
        </nav>
        <h1 id="735fcb7a-560a-41eb-a432-781047d2f08f">
            Plánování studia mimo Česko
        </h1>
        <p id="d3710422-dd05-4217-8364-45e774d7c90e">
            O tom, že chci studovat v zahraničí, jsem věděl několik let dopředu,
            ale příliš důkladně jsem nezkoumal, co vše takové rozhodnutí obnáší.
            Jen jsem tak postupně informoval své okolí (především rodiče) o této
            možnosti a občas sledoval videa studentů, kteří si touto zkušeností
            už prošli. Takové počínání vřele doporučuji studentům v prváku a ve
            druháku, protože na definitivní rozhodnutí je v této chvíli ještě
            dost času.
        </p>
        <p id="a2ea1ace-0fbf-44f5-926a-2afbf916a2b8">
            První důkladnější průzkum prostředí jsem poté uskutečnil na konci
            třetího ročníku gymnázia a o letních prázdninách. Na <a
                href="https://www.notion.so/">Notion</a
            > jsem si sepsal předběžný seznam univerzit, jejichž bakalářské programy
            mě alespoň trochu zaujaly. Věděl jsem, že chci studovat ve Skandinávii
            a rozhodně program v oblasti IT. Takové zúžení výběru hodně pomáhá, protože
            nabídka oborů v různých zemích v dnešní době překypuje možnostmi. A i
            přesto není lehké si vybrat.
        </p>
        <blockquote>
            S hledáním univerzity doporučuji začít na konci třetího ročníku.
            Zasílání přihlášek obvykle začíná kolem začátku roku, takže budete
            mít půl roku na přemýšlení.
        </blockquote>
        <h2 id="a8f80ebe-a970-4b8b-a9c9-568aa8176374">
            Kde hledat zahraniční univerzity
        </h2>
        <p id="7edd9b81-6048-442f-98eb-fcd3bf624b60">
            Velmi brzo jsem zúžil své možnosti pouze na Evropskou Unii, protože
            mé finanční možnosti měly stanovené jasné hranice a jen školné
            samotné mimo země EU dokáže obrátit rozpočet vzhůru nohama, nemluvě
            o dalších měsíčních výdajích.
        </p>
        <p id="c8f58075-d93a-49df-9ed1-f8a1c32c6c87">
            V tomto ohledu jsou užitečné stránky <a href="https://euroskop.cz/"
                >Euroskopu</a
            >, kde lze najít základní informace o mnoha zemích. Například
            <a href="https://euroskop.cz/ja-a-eu/studium/skolne-v-eu/">zde</a> jsou
            k dispozici přibližné ceny školného. Individuálně pak lze najít informace
            o systému výuky, možných stipendiích (na které bych však nespoléhal),
            nejznámějších univerzitách a taky základních údajů o ubytování, financích
            atd. od každé země.
        </p>
        <img
            src="euroskop.png"
            alt="Ukázka Euroskop.cz"
            description="Seznam školného v EU na Euroskop.cz"
        />
        <p id="a6c8a93d-527a-436c-91c2-9472fa566ab6">
            Jakmile jsem měl vybrané země (Švédsko, Finsko, Dánsko a Nizozemí),
            pomohla mi nejvíce <a
                href="https://www.bachelorsportal.com/search/bachelor?utm_source=studyportalsweb&utm_medium=organic"
                >tato stránka</a
            >. Jde o roztřizený seznam snad všech univerzitních programů z
            celého světa. Stačí zadat obor a lokalitu a během chvilky je na
            výběr z nespočtu možností. Na této stránce jsem si vždycky našel
            univerzitu, vyhledal si její stránky na Googlu a prošel si nabídky
            bakalářských oborů v angličtině. Pokud na následující rok univerzita
            nabízela program, který bych rád studoval, uložil jsem si jej opět
            do dokumentu na Notion.
        </p>
        <img
            src="bachelorsportal.png"
            alt="Ukázka Bachelorsportal"
            description="Seznam všech bakalářských programů na Bachelorsportal"
        />
        <p id="49224796-1325-4918-af47-3478868deacd">
            V této fázi jsem se nejvíce chtěl dostal na univerzitu do Dánska,
            druhé místo obsadilo Švédko a Finsko a nejméně se mi zamlouvalo
            Nizozemí. Nemělo to žádný racionální důvod, jen jsem to tak z
            nějakého důvodu cítil (jediné negativum Nizozemí bylo, že má jako
            jediné zpoplatněné studium, konkrétně cca 1000 € za první rok).
            Nakonec však vše dopadlo přesně naopak.
        </p>
        <p id="2b2e28c3-9a6c-45a1-873d-06b700ab2c1e">
            Dánsko zrovna na rok 2022 bohužel zrušilo naprostou většinu IT
            oborů, takže pro mě naprosto vypadlo ze hry. Dále jsem musel vyřadit
            i Švédsko a Finsko, protože životní výdaje v těchto zemích byly nad
            mé možnosti, například Švédsko odhaduje měsíční výdaje na 25 000 Kč,
            což si jednoduše nemohu dovolit (doporučuji v tomto ohledu vždy
            Googlit “study in <em>anglický název země</em>”, například
            <a href="https://studyinsweden.se/">Švédsko</a> vytvořilo nádherné a
            detailní užitečné stránky).
        </p>
        <p id="bb0eb081-af48-44a4-937a-3e0ee7eae125">
            Takže logicky zbývala poslední možnost: Nizozemsko. Co se týče
            financí, tak jsem našel, že lze očekávat měsíční výdaje kolem 600 €
            včetně ubytování a stravy + zmíněné školné, ale jsou k dispozici
            studentské granty, které by měly pokrýt velkou většinu. Našel jsem
            tři školy: Leiden, Groningen a Maastricht, všechny tři nabízely
            program Data Science &amp; Artificial Intelligence, což byl přímo
            obor, který jsem chtěl studovat. Takže na řadu přišly přijímačky.
        </p>
        <h2 id="e14969b3-ef26-45fa-8744-03a47171d30d">
            Přijímačky na nizozemských univerzitách
        </h2>
        <p id="c23a747b-2e5e-49a0-96cc-7a357f66f9ef">
            Groningen rychle odpadl z mých možností, protože zaprvé je poměrně
            oddělený od zbytku nizozemských měst a zadruhé byl program zde
            označený jako “Numerus Fixus”, což znamená, že vyberou pouze určitý
            počet z přihlášených lidí. V Maastrichtu a Leidenu brali všechny,
            jediné podmínky byly: angličtina alespoň na úrovni C1 a odmaturovat
            z matematiky. Toť vše, nic víc, nic míň. Přihlásit se tak může
            kdokoliv, i když nikdy předtím neviděl počítač. Je však nutné
            počítat s tím, že v prvním roce škola vyhodí velké množství
            studentů.
        </p>
        <figure
            class="block-color-gray_background callout"
            style="white-space:pre-wrap;display:flex"
            id="6c2c8fde-620b-44c3-8b7e-a787c2c1286f"
        >
            <div style="width:100%">
                Ostatní obory požadovaly motivační dopis nebo měly jiné
                požadavky, vždy je potřeba zkontrolovat si “Admission
                requirements” na příslušných stránkách a prokousat se
                nejednoznačnými informacemi napsanými v angličtině. Když si
                nejste jistí, napište univerzitě email, není se čeho bát.
            </div>
        </figure>
        <p id="ea969ae6-0e8f-4149-ba37-b80af6835ebc">
            Z nějakého důvodu chtěli v Leidenu za poslání přihlášky 100 €,
            zatímco v Maastrichtu byla zdarma. První verzi přihlášky jsem
            odevzdával kolem března, přičemž univerzita požadovala základní
            dokumenty (fotku, občanský průkaz, test z angličtiny) a poslední
            obdržené vysvědčení přeložené do angličtiny (tj. pololetní
            vysvědčení ze čtvrťáku). To mi ochotně přeložila kariérní poradkyně
            na mém gymnáziu. Poté univerzita zašle mail potvrzující podmínečné
            přijetí a seznam kroků, který je nutné splnit k definitivnímu
            přijetí. U mě to znamenalo dodat maturitní vysvědčení se zkouškou z
            matematiky (měl jsem pouze školní matematiku a stačilo to) a
            zaplatit školné. Deadline pro získání podmínečného přijetí byl konec
            května, na dodání zbylých dokumentů je čas až do konce srpna.
        </p>
        <p id="0603624b-79c0-481d-8631-fd8109bfeba2">
            Já jsem odevzdání maturitního vysvědčení nechal až na poslední
            chvíli, kdy jsem už byl v Maastrichtu a vše jsem odevzdal osobně na
            univerzitě. Předal jsem ověřenou kopii maturitního vysvědčení (v
            češtině) a pak dokument s anglickým překladem, který jsem dostal ze
            školy k samotnému vysvědčení. Vše prošlo bez problému a do dvou dnů
            mi univerzita potvrdila přijetí.
        </p>
        <p id="90a509f1-e029-449e-b6fd-79d0d4817983">
            Ale to jsem trochu předběhl, protože jsem ještě ani nenapsal, do
            kterého města jsem byl vlastně přijat. Situace se totiž měla takto:
        </p>
        <h2 id="d4fd899b-6cb4-4013-a35d-176c221bda45">
            Hledání studentského ubytování v zahraničí
        </h2>
        <p id="8aaa58d0-92c2-45b7-9623-4ad6a8b349d9">
            Předtím, než jsem začal vyplňovat přihlášky, jsem očekával, že
            největším oříškem bude papírování a komunikace s univerzitou. To
            jsem se ale šeredně mýlil, protože to proběhlo až na malé
            nesrovnalosti bez problému. Na obzoru se totiž objevil mnohem větší
            a náročnější protivník: hledání ubytování.
        </p>
        <figure>
            Hledání ubytování bylo jednoznačně nejtěžším úkolem při přípravě na
            studium v zahraničí. Začněte proto brzy!
        </figure>
        <p id="8525a98e-590f-487a-b103-d71f2d54afed">
            Pro někoho, kdo celý svůj život bydlel u rodičů a nikdy se
            ubytováním nezabýval, jde o nečekaně složitý úkol. Kdybych měl tento
            proces shrnout v jednom slově, byla by to beznaděj. V Nizozemsku ze
            zákona neexistují koleje, takže nemáte žádnou záruku ubytování. To
            navíc znamená, že si vše musíte zařídit sami - najít, zkontrolovat,
            podepsat… A poptávka enormně překročuje nabídku, z toho, co jsem
            pochopil, tak v celém Nizozemsku.
        </p>
        <h2 id="c3e32186-116a-4845-9483-afd8a6265e59">
            Úskalí při hledání ubytování
        </h2>
        <p id="c04e1117-1977-43d0-9514-fa9444d94aa2">
            Já ani vlastně nevím, jak situaci s ubytováním v Nizozemsku sepsat,
            protože to je opravdu naprostý zmatek s několika háčky a problémy,
            takže nejprve zde sepíšu v bodech pár tipů, a pak svou zkušenost:
        </p>
        <ul id="d2869ff1-6342-4f38-8f9e-739e852f8763" class="bulleted-list">
            <li style="list-style-type:disc">
                <b>S hledáním začněte nejpozději v březnu.</b> Není nutné něco najít,
                ale spíše si udělat obrázek. Pokud najdete něco pod 400 €, tak to
                berte jako jackpot a neváhejte.
            </li>
        </ul>
        <ul id="1b3532a0-c3c0-4826-8ca3-dc63edf10962" class="bulleted-list">
            <li style="list-style-type:disc">
                <b
                    >Zároveň ale buďte velmi ostražití, na trhu se pohybuje také
                    mnoho podvodníků.</b
                > Je nutné si (v angličtině) přečíst, co doporučuje univerzita při
                vyhýbání se podvodným nabídkám. Většinou je nutné nejprve podepsat
                smlouvu, až potom platit. Na smlouvě by mělo být jméno landlorda
                a jeho adresa: zkuste si tyto informace vygooglit a vyhodnotit, zda
                jsou tyto údaje věrohodné.
            </li>
        </ul>
        <ul id="0350f53e-ec23-4347-81c8-f21018dae017" class="bulleted-list">
            <li style="list-style-type:disc">
                <b
                    >Hned ze začátku rozšiřte své hledání i do okolí města, kde
                    budete studovat.</b
                > Vyplatí se zkusit blízké vesnice, kde je ubytování dostupnější
                a taky levnější. Dojíždění do školy pak sice zabere kolem 20 minut
                na kole, ale před vyučováním a po něm jde o zaslouženou relaxaci.
            </li>
        </ul>
        <ul id="8b5f9d7e-6753-469c-9c4e-41d192415283" class="bulleted-list">
            <li style="list-style-type:disc">
                <b>Univerzity obvykle nějaké ubytování nabízejí</b>, ale je
                vzhledem k počtu studentů velmi limitované. Takové nabídky jsou
                vždy velmi brzy rozebrané, dokonce možná už v březnu. Proto je
                nutné hledat rychle.
            </li>
        </ul>
        <ul id="5f511904-b93e-4e5f-8f43-6d87caf0cde2" class="bulleted-list">
            <li style="list-style-type:disc">
                <b>U každého ubytování si zjistěte podrobnosti.</b> Je v udávané
                ceně započtena elektřina, plyn a voda? Kde se ubytování nachází?
                S kolika lidmi budete na ubytování bydlet?
            </li>
        </ul>
        <ul id="e3123d54-2ee2-4b6e-b4d6-b0a07aa6387a" class="bulleted-list">
            <li style="list-style-type:disc">
                Když se mě kamarádi a rodina ptali na Nizozemí a já se jim
                zmínil o tristní situaci s ubytováním, <b
                    >všichni navrhovali hledat na Facebooku. To ale v podstatě
                    nemá cenu,</b
                > protože naprostá většina nabídek tam jsou podvody a zbytek je ihned
                rozebraný, na jakoukoliv nabídku je do pár minut několik komentářů.
                Facebook se hodí jedině k potkávání lidí ve stejné situaci. Poznal
                jsem takto jednoho Poláka, se kterým jsme si pak navzájem pomáhali.
                Případně můžete zkusit hledat ve více lidech, někdy tak můžete mít
                štěstí a najít nabídku celého apartmánu k pronájmu, což vás navíc
                vyjde levněji.
            </li>
        </ul>
        <ul id="e8f02434-9e6a-48ab-8550-58a22968edc6" class="bulleted-list">
            <li style="list-style-type:disc">
                Už během hledání ubytování počítejte s nutnými náklady. Nejenže
                nakonec stejně budete muset neznámému člověku poslat první
                splátku nájmu, nejprve budete muset pravděpodobně zaplatit za
                členství na inzerující stránce. Naprostá většina ubytování jsou
                nabízena na stránkách, které vám dovolí reagovat na nabídky
                pouze <b>po zaplacení členského příspěvku,</b> který většinou činí
                kolem 30 €. To samé mě potkalo i u univerzitních stránek.
            </li>
        </ul>
        <h2 id="1015a6b6-4df7-4ed0-9eba-19e72e932ef4">
            Mé zkušenosti s hledáním bytu
        </h2>
        <p id="d0d6e5ce-a431-4aeb-ac98-498ee789efd6">
            Já jsem hledání ubytování naivně podcenil. Říkal jsem si, že zrovna
            ubytování se nakonec nějak musí vyřešit, ale ve výsledku to byly mé
            největší obavy. Začal jsem kolem května a dva měsíce jsem neměl
            vůbec štěstí. Nabízející jsou obvykle zahlceni zprávami studentů a
            několikrát ani neodpovídají. To je velmi demotivující. A když pak
            vidíte, jak jsou poměrně levné nabídky ihned pryč a zbývají jenom
            možnosti 500 € + za měsíc, tak to sebevědomí taky moc nepomáhá.
        </p>
        <p id="6e3a2780-9981-49e5-827f-38ddd8d5c42f">
            V Maastrichtu jsem hledal především přes stránky univerzity, kde
            však byla neuvěřitelně velká konkurence, nejenže soupeříte s novými
            studenty, na trhu se nachází také studenti vyšších ročníků, takže o
            konkurenci není nouze. Dále jsem se díval na stránky Pararius, které
            však po kliknutí na nabídku přesměrují pouze na další stránky, kde
            je nutné zaplatit členství, a do toho už se mi moc nechtělo. V
            Leidenu jsem nenašel žádné přijatelné ubytování, což byl taky důvod,
            proč jsem nyní v Maastrichtu.
        </p>
        <img
            src="maastricht_housing.png"
            alt="Maastricht Housing"
            description="Oficiální stránka Maastricht University s nabídkou ubytování"
        />
        <p id="6111eda2-6439-4bd4-8779-e4fbfde14ecb">
            Tam jsem to nakonec musel vyřešit trochu neetickou (a pro čtenáře -
            vás - demotivující) cestou. Jelikož umím programovat, tak jsem si
            napsal program, který mi zavolal na mobil pokaždé, když se na
            stránkách objevila nová nabídka, abych tak vždycky byl první, kdo na
            ní odpoví. To se mi asi čtyřikrát povedlo a měl jsem díky tomu dvě
            odpovědi - obě v Belgii (jelikož Maastricht je přímo na hranicích,
            tak to je volba, ke které se nakonec hodně studentů pocházejících z
            EU přikloní). Toto se stalo na začátku srpna.
        </p>
        <details>
            <summary>Odkaz na skript (pro programátory)</summary>
            <a
                href="https://github.com/Pavlyuchenko/AutomizationBotMaastrichtHousing"
                >https://github.com/Pavlyuchenko/AutomizationBotMaastrichtHousing</a
            >
        </details>
        <p id="d2191eb3-d5d9-497f-bd27-7f56998b995f">
            Tím však trable zdaleka neskončily. Landlord odpovídal lámanou
            angličtinou a velice stručně, což nepodpořilo mou důvěru v něj.
            Navíc poslal amatérsky sepsanou smlouvu ve fontu Comic Sans, což už
            na mě bylo moc. Ale jelikož jsme se spojili přes stránky univerzity,
            tak jsem to risknul a poslal zálohu 325 € a doufal. Nakonec se
            ükázalo, že jde o staršího pána, který je velice příjemný. Velké
            štěstí jsem měl také v ceně, protože platím pouze 325 € měsíčně za
            vlastní pokoj se sdílenou koupelnou a kuchyní ve studentském domě.
            Jen teda dojíždím každý den (někdy i dvakrát, když máme místo mezi
            přednáškami) 25 minut na univerzitu a 25 minut zpátky.
        </p>
        <h2 id="dd45c0f5-7465-4ea3-a26a-525df63e5c9e">
            Co je třeba zařídit před odjezdem na zahraniční univerzitu
        </h2>
        <p id="74196902-c334-4dff-99d4-344cd9d500cb">
            Zde uvádím seznam nejen formálních záležitostí, které musíte zařídit
            před odjezdem:
        </p>
        <ol
            type="1"
            id="76386a46-b64d-4d73-9c4e-96ade3364684"
            class="numbered-list"
            start="1"
        >
            <li>
                <b>Být podmínečně přijat na své univerzitě.</b> To obvykle vyžaduje
                přeložené pololetní vysvědčení z angličtiny, anglický certifikát
                na úrovni C1 (B2 může taky někdy stačit) a potenciálně motivační
                dopis.
            </li>
        </ol>
        <ol
            type="1"
            id="47b867d5-d294-497d-aefc-7052885b2323"
            class="numbered-list"
            start="2"
        >
            <li>
                <b>Mít za sebou úspěšně složenou maturitní zkoušku.</b> S sebou si
                vzít originální maturitní vysvědčení, ověřenou kopii (musíte s originálem
                zajít na poštu) a překlad do různých jazyků, ten byste měli obdržet
                s maturitním vysvědčením při slavnostním předávání.
            </li>
        </ol>
        <ol
            type="1"
            id="33cae2ed-f37a-4279-b240-a27e0fd1224c"
            class="numbered-list"
            start="3"
        >
            <li><b>Mít v zahraničí zařízené ubytování</b></li>
        </ol>
        <ol
            type="1"
            id="8d36b423-ac93-47bc-8aca-acd1279166af"
            class="numbered-list"
            start="4"
        >
            <li>
                <b>Vlastní bankovní účet a internetové bankovnictví</b>, ideálně
                v měně země, do které jedete. Zatímco Raiffeisenbanka si účtuje
                300 Kč za každý převod na zahraniční účet, Revolut nemá žádné
                poplatky.
            </li>
        </ol>
        <ol
            type="1"
            id="aa564451-cd6e-4060-b701-6d1b2462ffa9"
            class="numbered-list"
            start="5"
        >
            <li>
                <b
                    >Zjistit si u pojišťovny, zda vaše pojištění platí i v
                    zahraničí</b
                >
                a zda je třeba mít potvrzení o tom, že jste i nadále studentem (to
                je poměrně důležité, jinak si budete pojištění muset měsíčně platit).
            </li>
        </ol>
        <ol
            type="1"
            id="d6652d89-fb56-4cbb-ac0f-27d6b552c85b"
            class="numbered-list"
            start="6"
        >
            <li>
                <b>Mít zaručený dostatečný měsíční finanční příjem</b> = nájem +
                cca 200 €. A počítat s tím, že první měsíc zaplatíte alespoň dvojnásobek,
                u mě to bylo 1 100 €.
            </li>
        </ol>
        <p id="f13815a3-08c3-4bc5-b251-4ec3d4725616">
            To je pravděpodobně vše, co je nutné. Vždy si zjistěte, zda vaše
            univerzita nepožaduje ještě nějaké dodatečné formality.
        </p>
        <h1 id="ffea702d-01d3-4cad-92ee-fc95c1f3192d">Odjezd do zahraničí</h1>
        <h2 id="2eb72d00-8d7d-442d-8de1-89041bb8fdc3">Pocity před odjezdem</h2>
        <p id="f79a1f0c-e357-4bf0-aaca-76ed911e033f">
            Čím víc se blížil odjezd, tím víc mi cizina nahnávala neskutečnou
            hrůzu a tím víc jsem začal tohoto rozhodnutí litovat. Poprvé mi
            docházelo, k čemu jsem se to vlastně odsoudil. Poprvé neuvidím své
            rodiče několik měsíců v kuse, po příchodu z univerzity budu na
            ubytování doma sám, odkázaný pouze a jen na sebe. A aby toho nebylo
            málo, opouštím všechny své kamarády. Co když už si s nikým nebudu
            rozumět, když se vrátím o Vánocích zpátky? A co hůř, co když si
            nenajdu žádné kamarády v Nizozemí?
        </p>
        <blockquote>
            Týden před odjezdem byl zdaleka nejhorší zážitek, ještě horší než
            stres z maturity. Všechno utíká neskutečně rychle a začínáte si
            uvědomovat, že opouštíte všechny své kamarády i rodinu.
        </blockquote>
        <p id="2d7bd071-df75-41fe-af22-866d9923aa7f">
            A můžu říct, že dny ubíhají rychleji a rychleji čím víc se blížíte
            ke dni odjezdu. Poslední týden v Česku jsem byl v takovém podivném
            stavu, kdy jsem se opravdu bál následujících několika týdnů a bylo
            divné uvědomit si, že se všechny známé teď několik měsíců neuvidím.
            Ale nějak jsem to při loučení nepociťoval, nevím přesně proč, bylo
            toho na mě opravdu hodně v krátkém intervalu. Je vhodné být alespoň
            psychicky připravený na to, že takový moment nastane.
        </p>
        <h2 id="6fb013a0-4f13-4c96-9ce6-ab988d86e0ef">
            Seznamovací týden na univerzitě
        </h2>
        <p id="98275e86-892a-4972-87fd-77f2dfc5527e">
            Největší strach jsem však měl ještě z jedné skutečnosti, kterou jsem
            zatím nezmínil. Do svého ubytování jsem se mohl nastěhovat 27.
            srpna, ale ještě týden předtím se konal seznamovací týden (který mě
            stál 60 €), v průběhu něhož jsem tedy neměl kde bydlet. Hotely v
            Nizozemsku jsou na můj rozpočet nehorázně předražené. Zbývaly mi dvě
            možnosti. První byla zavolat na své ubytování a zeptat se, jestli
            bych se nemohl ubytovat dříve. Druhá byla spoléhat se na samotný
            seznamovací týden, protože na stránkách nezávazně slibovali možnost
            přespání buď u studentské asociace nebo u mentorů, kteří budou
            přidělení každé skupině.
        </p>
        <p id="ed308070-049c-4dfa-a95b-91256af90d7a">
            Měl jsem tedy velké nervy, protože ani jedna možnost nebyla
            stoprocentní. Nakonec jsem si pro klid duše na první noc koupil
            ubytování v hostelu <a href="https://www.stayokay.com/en"
                >StayOkay</a
            > za 1000 Kč. To mě celkem zachránilo, protože jinak bych do Maastrichtu
            dorazil v čtyři hodiny ráno a neměl kam jít, tak jsem si mohl schovat
            zavazadla do hotelu a odpočívat po náročné cestě v teple (ubytování jsem
            měl objednané až na následující noc). Na zbytek týdne mi nakonec landlord
            našel jeden volný pokoj, ve kterém jsem mohl strávit pár dní, než se
            uvolní můj pokoj. Pak jsem také během seznamovacího týdne strávil dvě
            noci u svých mentorů (kteří byli opravdu super a se vším mi pomáhali),
            protože mé ubytování bylo 25 minut daleko na kole, kolo jsem já však
            neměl.
        </p>
        <p id="e7166e66-418f-4875-93a5-f0cf785d386e">
            Seznamovací týden bych určitě bez váhání doporučil, jestli taková
            událost na vaší univerzitě existuje. V Maastrichtu se jmenuje INKOM
            a organizují jej každoročně studenti. Pro mě, introverta, to sice
            byla celkem stresující a vyčerpávající zkušenost, když jsem se navíc
            první den cítil sklíčeně a několikrát se mi i zničehonic vehnaly
            slzy do očí. Jste nuceni začínat několik opakujících se konverzací s
            různými studenty, pokaždé se představovat, odkud jste, co studujete
            a tak dále, což je už po desáté celkem frustrující. Nutno však říci,
            že jsem díky tomu poznal hodně lidí a našel si pár kamarádů, se
            kterými se sem tam stýkám i nadále navzdory tomu, že studujeme na
            opačné straně města.
        </p>
        <blockquote>
            Jestli vaše univerzita nabízí seznamovací týden, vřele doporučuji se
            jej zúčastnit. Je to sice psychicky náročné, ale dost vám to ze
            startu v cizím městě pomůže a najdete si alespoň pár kamarádů.
        </blockquote>

        <p id="7ab74da0-6b0d-4ef6-bf93-f23d6330ef00">
            Při výběru univerzity je také nutné uvažovat racionálně. Jako
            příklad uvedu, že Maastricht University se na svých stránkách chlubí
            více než 50 % studenty ze zahraničí. Vyhledejte si však Maastricht
            na mapě a zkuste zapřemýšlet, jaký v tom potenciálně může být háček.
            Ano, nachází se v bezprostřední blízkosti hranic s Belgií a
            Německem. A opravdu tomu je tak, že dvě třetiny z 50 % mezinárodních
            studentů jsou buďto z Belgie, a tudíž mluví nizozemsky, nebo z
            Německa. A třeba program International Business je v zásadě pouze
            německou záležitostí. Je proto nutné se vždy zamyslet nad některými
            informacemi a zvážit, zda tomu opravdu je tak, jak se na internetu
            píše, a podle toho se pak rozhodnout.
        </p>
        <h2 id="451ff8c2-30d0-4852-8e2a-4049cc1c1cd2">
            Hledání kamarádů v zahraničí
        </h2>
        <p id="ab72d28f-51b8-46a8-b70d-c2bd27308f95">
            Co se týče kamarádů, prvních pár měsíců nebudete k nikomu cítit
            stejně silné pouto, jaké jste si vybudovali s lidmi v průběhu
            střední školy. To ve vás zanechá pocit prázdnoty, protože několik
            týdnů budou všichni, které máte rádi, několik stovek kilometrů od
            vás a setkání s nimi často v nedohlednu.
        </p>
        <p id="f2b96ecb-b978-413a-a029-b50062c3549e">
            Pro mě bylo hledání nových kamarádů celkem oříšek. Nečekal jsem, že
            to pro mě bude tak těžká výzva. Před univerzitou jsem totiž studoval
            na osmiletém gymnáziu, což co se týče kamarádů znamená, že jste 8
            let naprosto v suchu a nejste nutně vystaveni potřebě hledat si nové
            přátele. v zahraničí dramaticky mění. Neznáte naprosto nikoho, a
            když se s někým “skamarádíte”, trvá to dlouhou dobu, než se
            vyrovnají vašim kamarádům doma.
        </p>
        <p id="f4b06c62-ef0f-4f68-a734-e8dc4aa50661">
            Uklidňující (aspoň pro mě) bylo, že v na vysoké škole v Česku by to
            nebylo o moc jiné. Tam se taky zas tak často se svými předchozími
            kamarády nevídáte a musíte si najít nové. Zahraničí má tu výhodu, že
            tady se několik lidí nachází v naprosto stejné situaci jako vy. To
            je dobré, protože všichni jsou naprosto otevření novým lidem, takže
            jsem za celou dobu v Maastrichtu nenarazil na nikoho, kdo by se se
            mnou nechtěl aspoň trochu pobavit. Když se vám někdo na pohled
            zamlouvá, nic nedáte za to to zkusit a nejspíš zjistíte, že on/ona
            se s vámi chce bavit také. Zapamatujte si:
        </p>
        <figure id="aae437c7-9a8a-408c-9aaf-f262f201055f">
            Všichni na tom jsou na zahraničí univerzitě ze začátku stejně: jsou
            vystresovaní a chtějí si hlavně najít kamarády. Proto se nebojte
            začínat náhodné konverzace s lidmi, kteří vám přijdou sympatičtí.
        </figure>
        <h1 id="4033e36a-ba09-407e-bae3-808013c26314">
            Studovat na univerzitě v zahraničí?
        </h1>
        <p id="2365c3d0-1f09-41d4-91c1-050539fdfa68">
            Tím se dostáváme k vyústění tohoto článku. Vyplatí se studovat v
            zahraničí? Co se týče získaných zkušeností a osamostatnění se, není
            o čem diskutovat. Pro budoucí kariéru jde o nenahraditelnou výhodu
            oproti konkurenci a vynucená samota a naprosto nové prostředí
            pomohou v osobním růstu.
        </p>
        <p id="023f3550-0564-42ec-b9e2-7ae36d532cc4">
            V krátkodobém hledisku však jde o obrovskou výzvu. Ocitáte se v
            novém světě a na každém kroku zpochybňujete svá rozhodnutí a
            uvědomujete si, co všechno jste nechali za sebou. A navíc se z toho
            nedá jednoduše vycouvat. Jednou jste se rozhodli a musíte za to nést
            zodpovědnost stůj co stůj a doufat, že vše dobře dopadne. A u toho
            si být vědom, že nejsme v pohádce, takže to dobře dopadnout nemusí.
        </p>
        <p id="c62be239-5b8e-45fc-9b7d-397f5fb0066e">
            Tímto článkem jsem nechtěl nikoho vystrašit ani odradit od studia v
            zahraničí, pouze donutit k zamyšlení. Zahraničí totiž není pro
            každého a není to ani zdaleka jednoduché, jak to může někomu
            připadat. Jde o velké rozhodnutí, které nemůžete dopodrobna
            promyslet, protože jde o krok do neznáma a jen čas ukáže, zda jste
            se rozhodli správně. Proto rozhodujte trpělivě a důkladně.
        </p>
    </div>
</section>

<style>
    .first-paragraph::first-letter {
        font-size: 50px;
        font-weight: 700;
        float: left;
        margin-right: 10px;

        line-height: 1;
    }

    #title {
        text-align: center;
        margin-top: 50px;
        margin-bottom: 5px;
        font-size: 46px;
        color: var(--primary);
    }
    #article-details {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 35px;
        font-size: 17px;

        font-weight: 700;
    }
    #article-details span {
        color: var(--secondary);
    }
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        margin-top: 30px;
    }
    section * {
        max-width: 800px;
        line-height: 29px;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        text-align: left;

        color: var(--primary);
    }
    .table_of_contents {
        margin-top: 30px;
        margin-bottom: 30px;

        padding-left: 20px;
    }
    .table_of_contents-item {
        line-height: normal;
        margin-top: 3px;
    }
    .table_of_contents-indent-1 {
        padding-left: 20px;
    }

    .table_of_contents-link {
        font-size: 14px;
        font-weight: 400;

        line-height: 0;
        color: #999;
        transition: 0.15s;
    }
    .table_of_contents-link:hover {
        color: #333;
    }
    h1 {
        font-size: 32px;
        font-weight: 500;

        margin-top: 75px;
    }
    h2 {
        font-size: 25px;
        font-weight: 500;

        margin-top: 45px;
    }
    a {
        color: var(--primary);
        font-weight: 600;
    }
    p {
        font-size: 18px;
    }

    blockquote {
        position: relative;

        margin-left: 0;
        padding-left: 30px;
        margin-top: 35px;
        margin-bottom: 35px;
    }
    blockquote::before {
        content: "";
        display: inline-block;

        position: absolute;
        left: 0;
        top: -5px;

        width: 6px;
        height: calc(100% + 10px);

        background-color: black;
    }

    figure {
        background-color: var(--primary);
        color: #fff;

        margin: 0;
        padding: 20px 30px;
        white-space: normal !important;

        border-radius: 8px;

        margin: 40px 0;
    }

    @media (max-width: 800px) {
        #title {
            font-size: 32px;
        }
        #article-details {
            font-size: 13px;
            font-weight: 400;
            gap: 8px;
        }
        #article {
            margin-top: 10px;
        }
        h1,
        h2,
        h3,
        h4,
        h5,
        h6 {
            line-height: normal;
        }
        h1 {
            font-size: 28px;
            margin-top: 50px;
        }

        figure {
            padding: 15px 25px;
        }
    }
</style>
