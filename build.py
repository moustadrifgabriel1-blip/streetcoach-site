# Assemble les pages du site a partir d'un gabarit commun. Aucune dependance :
#   python3 build.py
EMAIL = "moustadrifecomm@gmail.com"
EDITEUR = "Gabriel Moustadrif"
MAJ = "20 septembre 2026"

def page(fichier, titre, description, corps, accueil=False):
    p = "" if accueil else "index.html"
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#16181C">
<meta property="og:title" content="{titre}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="img/frontlever.jpg">
<link rel="icon" href="img/icone.png">
<link rel="apple-touch-icon" href="img/icone.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,600..900&family=Geist:wght@400;500;700&family=Martian+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="nav"><div class="wrap">
  <a class="brand" href="index.html"><img src="img/icone.png" alt="" width="32" height="32">StreetCoach</a>
  <nav aria-label="Navigation principale">
    <a class="opt" href="{p}#methode">La méthode</a>
    <a class="opt" href="{p}#figures">Les figures</a>
    <a href="support.html">Support</a>
  </nav>
</div></header>
<main>
{corps}
</main>
<footer><div class="wrap">
  <div>© 2026 StreetCoach. Édité par {EDITEUR}, Suisse.</div>
  <nav aria-label="Liens légaux">
    <a href="confidentialite.html">Confidentialité</a>
    <a href="support.html">Support</a>
    <a href="supprimer-compte.html">Supprimer mon compte</a>
    <a href="mailto:{EMAIL}">Contact</a>
  </nav>
</div></footer>
</body>
</html>
"""
    open(fichier, "w", encoding="utf-8").write(html)

# ---------------------------------------------------------------- accueil
page("index.html",
     "StreetCoach, ton coach de street workout",
     "Des séances de street workout courtes et intenses, composées pour toi. Progression automatique, figures à débloquer, Apple Watch. Fonctionne hors ligne.",
     f"""
<section class="hero"><div class="wrap">
  <div>
    <span class="label">Street workout et calisthénie</span>
    <h1 style="margin-top:16px">La barre, un plan, <em>des progrès.</em></h1>
    <p class="lead">StreetCoach compose ta séance du jour, suit chaque série et décide quand tu montes en charge. Toi, tu t'entraînes.</p>
    <div class="cta">
      <span class="btn primary" aria-disabled="true">Bientôt sur l'App Store</span>
      <a class="btn ghost" href="#methode">Voir comment ça marche</a>
    </div>
    <p class="note">iPhone et Apple Watch. Fonctionne au parc, sans réseau.</p>
  </div>
  <figure><img src="img/frontlever.jpg" alt="Athlète tenant un front lever à la barre" width="768" height="768"></figure>
</div></section>

<section class="alt" id="methode"><div class="wrap">
  <div class="head">
    <span class="label">La méthode</span>
    <h2>Court, intense, et toujours un cran plus loin</h2>
    <p>Pas de programme figé à suivre pendant douze semaines. Chaque séance part de ce que tu as réellement fait la dernière fois.</p>
  </div>
  <div class="grid">
    <div class="card"><span class="k">01</span><h3>35 à 45 minutes</h3><p>Cinq exercices au plus. Une séance qui déborde est une séance qu'on écourte au hasard, alors le coach tranche avant toi.</p></div>
    <div class="card"><span class="k">02</span><h3>La charge monte toute seule</h3><p>Objectif tenu proprement, tu montes. Reps au plafond, le coach ajoute du lest. Série arrachée, il consolide. Tu notes tes reps, il décide.</p></div>
    <div class="card"><span class="k">03</span><h3>Trois semaines, puis on souffle</h3><p>Une semaine de décharge est planifiée après trois semaines de charge. C'est là que les tendons rattrapent les muscles.</p></div>
    <div class="card"><span class="k cool">04</span><h3>Ton état compte</h3><p>Sommeil, variabilité cardiaque, pouls au repos : l'app lit ce que ta montre a mesuré cette nuit et allège la séance quand il le faut.</p></div>
    <div class="card"><span class="k cool">05</span><h3>La barre est prise ?</h3><p>Remplace un exercice par une variante du même mouvement, ou écarte le. Un exercice écarté n'est jamais compté comme un échec.</p></div>
    <div class="card"><span class="k cool">06</span><h3>Au poignet</h3><p>Chrono de repos, exercice en cours et fréquence cardiaque sur Apple Watch. Le repos s'affiche aussi sur l'écran verrouillé.</p></div>
  </div>
</div></section>

<section id="figures"><div class="wrap">
  <div class="head">
    <span class="label">Les figures</span>
    <h2>Vise une étape, pas un rêve</h2>
    <p>Quarante cinq figures, du L-sit à la planche. Personne ne passe de zéro au front lever complet : tu vises le tuck, puis l'advanced tuck, puis le straddle. Le coach programme l'étape et te dit si tu es dans les temps.</p>
  </div>
  <div class="figures">
    <figure><img src="img/lsit.jpg" alt="L-sit" width="768" height="768" loading="lazy"><figcaption>L-sit</figcaption></figure>
    <figure><img src="img/frontlever.jpg" alt="Front lever" width="768" height="768" loading="lazy"><figcaption>Front lever</figcaption></figure>
    <figure><img src="img/planchestraddle.jpg" alt="Planche straddle" width="768" height="768" loading="lazy"><figcaption>Planche straddle</figcaption></figure>
    <figure><img src="img/humanflag.jpg" alt="Drapeau" width="768" height="768" loading="lazy"><figcaption>Drapeau</figcaption></figure>
  </div>
</div></section>

<section class="alt"><div class="wrap split">
  <div>
    <span class="label">Tes données</span>
    <h2 style="margin-top:12px">Elles restent sur ton téléphone</h2>
    <p class="muted" style="margin-top:16px">StreetCoach fonctionne entièrement hors ligne. Aucun compte n'est nécessaire, aucune publicité, aucun traceur. Si tu crées un compte, c'est uniquement pour retrouver ton historique sur un autre téléphone.</p>
    <p><a href="confidentialite.html">Lire la politique de confidentialité</a></p>
  </div>
  <ul class="check">
    <li>Séances composées sur l'appareil, sans serveur</li>
    <li>Données de santé lues sur l'iPhone, jamais envoyées</li>
    <li>Ressenti dicté, transcrit sur l'appareil</li>
    <li>Sauvegarde iCloud automatique, compte en ligne facultatif</li>
    <li>Suppression du compte et des données en un geste</li>
  </ul>
</div></section>
""", accueil=True)

# ---------------------------------------------------------- confidentialite
page("confidentialite.html",
     "Politique de confidentialité, StreetCoach",
     "Quelles données StreetCoach traite, où elles vivent, et comment les supprimer.",
     f"""
<article class="doc"><div class="wrap">
<span class="label">Document légal</span>
<h1>Politique de confidentialité</h1>
<p class="muted">Dernière mise à jour : {MAJ}</p>

<div class="box"><strong>En bref.</strong> StreetCoach fonctionne hors ligne et garde tes données sur ton téléphone. Pas de publicité, pas de traceur, pas de revente. Un compte en ligne est facultatif et ne sert qu'à sauvegarder ton historique. Tu peux tout supprimer à tout moment, depuis l'app.</div>

<h2>1. Qui est responsable</h2>
<p>L'application StreetCoach est éditée par {EDITEUR}, développeur indépendant établi en Suisse, responsable du traitement au sens de la loi fédérale suisse sur la protection des données (nLPD) et du règlement général sur la protection des données (RGPD).</p>
<p>Contact pour toute question ou demande : <a href="mailto:{EMAIL}">{EMAIL}</a></p>

<h2>2. Les données traitées</h2>
<div class="scroll"><table>
<thead><tr><th>Donnée</th><th>À quoi elle sert</th><th>Où elle se trouve</th></tr></thead>
<tbody>
<tr><td>Profil : poids, âge, taille, matériel, objectif</td><td>Régler la charge, les temps de repos et les exercices proposés</td><td>Sur ton téléphone</td></tr>
<tr><td>Entraînements : séances, répétitions, lest, effort ressenti, objectifs</td><td>Calculer ta progression et composer la séance suivante</td><td>Sur ton téléphone</td></tr>
<tr><td>Données de santé lues dans Apple Santé : variabilité cardiaque, pouls au repos, sommeil, fréquence cardiaque pendant la séance</td><td>Estimer ta récupération et adapter la séance</td><td>Lues sur ton téléphone. Jamais envoyées à nos serveurs, jamais partagées</td></tr>
<tr><td>Données écrites dans Apple Santé : séance d'entraînement, durée, calories actives</td><td>Tenir ton historique d'activité dans Santé</td><td>Dans Apple Santé, sous ton contrôle</td></tr>
<tr><td>Ressenti dicté</td><td>Garder une note de fin de séance</td><td>L'audio est transcrit sur ton téléphone par le moteur d'Apple, puis supprimé. Seul le texte est conservé, sur ton téléphone</td></tr>
<tr><td>Adresse e-mail et mot de passe (seulement si tu crées un compte)</td><td>T'identifier pour la sauvegarde en ligne</td><td>Chez notre hébergeur, le mot de passe sous forme hachée</td></tr>
<tr><td>Fichier de sauvegarde (seulement si tu as un compte)</td><td>Restaurer ton historique sur un autre téléphone</td><td>Chez notre hébergeur, dans un espace privé accessible à toi seul</td></tr>
</tbody></table></div>
<p>Le fichier de sauvegarde contient ton profil et tes entraînements. Il ne contient aucune donnée lue dans Apple Santé : ces mesures servent à régler la séance du jour, puis ne sont pas conservées.</p>

<h2>3. Ce que nous ne faisons pas</h2>
<ul>
<li>Aucune publicité et aucun traceur publicitaire.</li>
<li>Aucun outil d'analyse d'audience dans l'application.</li>
<li>Aucune vente, location ou cession de données à des tiers.</li>
<li>Aucune utilisation des données de santé à des fins de marketing, de publicité ou de profilage, conformément aux règles d'Apple sur HealthKit.</li>
</ul>

<h2>4. Base légale</h2>
<p>Les données de l'application sont traitées pour exécuter le service que tu demandes. L'accès à Apple Santé, au microphone et à la reconnaissance vocale repose sur ton consentement, donné dans les fenêtres d'autorisation d'iOS, et que tu peux retirer à tout moment dans Réglages. La création d'un compte est volontaire.</p>

<h2>5. Sous-traitants et lieu d'hébergement</h2>
<ul>
<li><strong>Supabase</strong> (hébergement du compte et de la sauvegarde). Les données sont stockées dans un centre de données situé à Zurich, en Suisse.</li>
<li><strong>Brevo</strong> (envoi des e-mails du compte : confirmation d'adresse, réinitialisation du mot de passe). Seule ton adresse e-mail lui est transmise, uniquement pour acheminer ces messages. Brevo est une société française, les données sont traitées dans l'Union européenne.</li>
<li><strong>Apple iCloud</strong>. Si iCloud Drive est activé sur ton appareil, une copie de sauvegarde est placée dans ton propre espace iCloud. Elle relève de ton compte Apple, nous n'y avons pas accès.</li>
</ul>

<h2>6. Durée de conservation</h2>
<p>Les données sur ton téléphone sont conservées tant que l'application est installée. Les données du compte sont conservées jusqu'à ce que tu supprimes ton compte. La suppression est immédiate et définitive : compte, profil et fichier de sauvegarde sont effacés de nos serveurs.</p>

<h2>7. Tes droits</h2>
<p>Tu peux accéder à tes données, les rectifier, les exporter et les supprimer :</p>
<ul>
<li><strong>Exporter</strong> : Profil, Sauvegarde et restauration, Sauvegarder maintenant. Le fichier apparaît dans l'app Fichiers.</li>
<li><strong>Supprimer ton compte</strong> : Profil, Compte en ligne, Supprimer mon compte. Voir aussi <a href="supprimer-compte.html">la page dédiée</a>.</li>
<li><strong>Tout effacer du téléphone</strong> : désinstaller l'application.</li>
</ul>
<p>Pour toute autre demande, écris à <a href="mailto:{EMAIL}">{EMAIL}</a>. Une réponse t'est donnée sous trente jours. Tu peux aussi saisir l'autorité de protection des données de ton pays, en Suisse le Préposé fédéral à la protection des données et à la transparence.</p>

<h2>8. Sécurité</h2>
<p>Les échanges avec nos serveurs sont chiffrés. Chaque compte n'a accès qu'à son propre espace, par des règles appliquées côté serveur. Les mots de passe ne sont jamais stockés en clair.</p>

<h2>9. Mineurs</h2>
<p>L'application ne s'adresse pas aux enfants de moins de 13 ans. La création d'un compte est réservée aux personnes de 16 ans et plus, ou disposant de l'accord de leur représentant légal.</p>

<h2>10. Avertissement santé</h2>
<p>StreetCoach est un outil d'entraînement, pas un dispositif médical. Les indications de récupération sont des estimations et ne remplacent pas un avis médical. Consulte un professionnel de santé avant de commencer un programme sportif si tu as un doute sur ton état.</p>

<h2>11. Modifications</h2>
<p>Cette politique peut évoluer. La date en tête de page indique la dernière mise à jour. Tout changement important sera signalé dans l'application.</p>
</div></article>
""")

# ------------------------------------------------------------------ support
page("support.html",
     "Support, StreetCoach",
     "Aide et contact pour l'application StreetCoach.",
     f"""
<article class="doc"><div class="wrap">
<span class="label">Aide</span>
<h1>Support</h1>
<p class="muted">Une question, un bug, une idée ? Écris à <a href="mailto:{EMAIL}">{EMAIL}</a>. Réponse sous deux jours ouvrés.</p>

<h2>Questions fréquentes</h2>

<h3>L'app fonctionne sans réseau ?</h3>
<p>Oui, entièrement. Les séances sont composées sur ton téléphone. Le réseau ne sert qu'à la sauvegarde en ligne, si tu as créé un compte.</p>

<h3>Faut il créer un compte ?</h3>
<p>Non. Le compte est facultatif et sert uniquement à retrouver ton historique sur un autre téléphone. Sans compte, une copie de sauvegarde part quand même dans ton iCloud si iCloud Drive est activé.</p>

<h3>Je change de téléphone, comment garder mon historique ?</h3>
<p>Sur le nouveau téléphone, installe StreetCoach, puis va dans Profil. Avec un compte : Compte en ligne, connecte toi, Restaurer sur ce téléphone. Sans compte : Sauvegarde et restauration, section iCloud, avec le même identifiant Apple.</p>

<h3>La carte « Ta montre cette nuit » n'apparaît pas</h3>
<p>Vérifie dans Réglages, Santé, Accès aux données et appareils, StreetCoach, que la lecture du sommeil, de la variabilité cardiaque et de la fréquence cardiaque au repos est autorisée. Il faut aussi porter la montre la nuit, et environ sept jours de mesures pour établir ta normale.</p>

<h3>Le coach ne me propose pas de lest</h3>
<p>Dans Profil, coche Gilet lesté dans ton matériel et indique sa charge maximale. Le lest est ajouté quand tes répétitions atteignent le plafond de la zone de travail.</p>

<h3>L'app sur Apple Watch ne se met pas à jour</h3>
<p>Ouvre l'app Watch sur l'iPhone, descends jusqu'à StreetCoach et touche Installer.</p>

<h3>Je n'ai pas reçu l'e-mail de confirmation</h3>
<p>Regarde dans les courriers indésirables. Si rien n'arrive après dix minutes, écris nous depuis l'adresse concernée.</p>

<h3>Comment supprimer mon compte ?</h3>
<p>Dans l'app : Profil, Compte en ligne, Supprimer mon compte. Détails sur <a href="supprimer-compte.html">la page dédiée</a>.</p>

<div class="box"><strong>Avertissement.</strong> StreetCoach n'est pas un dispositif médical. En cas de douleur, arrête l'exercice. En cas de doute sur ton état de santé, consulte un professionnel avant de t'entraîner.</div>
</div></article>
""")

# -------------------------------------------------------- suppression compte
page("supprimer-compte.html",
     "Supprimer mon compte, StreetCoach",
     "Comment supprimer ton compte StreetCoach et toutes les données associées.",
     f"""
<article class="doc"><div class="wrap">
<span class="label">Compte</span>
<h1>Supprimer mon compte</h1>
<p class="muted">La suppression est immédiate, définitive, et se fait depuis l'application.</p>

<h2>Depuis l'application</h2>
<ol>
<li>Ouvre StreetCoach, puis Profil.</li>
<li>Touche Compte en ligne.</li>
<li>Touche Supprimer mon compte, puis confirme.</li>
</ol>

<h2>Ce qui est supprimé</h2>
<ul>
<li>Ton compte (adresse e-mail et mot de passe).</li>
<li>Ton profil sur nos serveurs.</li>
<li>Ton fichier de sauvegarde en ligne.</li>
</ul>
<p>Rien n'est conservé après la suppression. L'historique présent sur ton téléphone n'est pas touché : pour l'effacer aussi, désinstalle l'application. La copie éventuelle dans ton iCloud se gère depuis Réglages, ton nom, iCloud, Gérer le stockage.</p>

<h2>Tu n'as plus accès à l'application ?</h2>
<p>Écris à <a href="mailto:{EMAIL}">{EMAIL}</a> depuis l'adresse e-mail du compte, avec pour objet « Suppression de compte ». La suppression est effectuée sous sept jours, et confirmée par e-mail.</p>
</div></article>
""")

# ------------------------------------------------------ e-mail confirme
page("compte-confirme.html",
     "Adresse confirmée, StreetCoach",
     "Ton adresse e-mail est confirmée.",
     """
<div class="ok">
  <div class="rond" aria-hidden="true"></div>
  <h1 style="font-size:clamp(2rem,6vw,3.2rem)">Adresse confirmée</h1>
  <p class="muted" style="max-width:32em;margin:20px auto 0">Ton compte StreetCoach est actif. Retourne dans l'application, puis connecte toi avec ton e-mail et ton mot de passe.</p>
</div>
""")
# ------------------------------------------------- nouveau mot de passe
page("nouveau-mot-de-passe.html",
     "Nouveau mot de passe, StreetCoach",
     "Choisis un nouveau mot de passe pour ton compte StreetCoach.",
     """
<article class="doc"><div class="wrap" style="max-width:460px">
<span class="label">Compte</span>
<h1>Nouveau mot de passe</h1>
<p class="muted" id="intro">Choisis un nouveau mot de passe, d'au moins 8 caractères.</p>
<form id="f" novalidate>
  <label for="mdp" class="label" style="display:block;margin:24px 0 8px">Nouveau mot de passe</label>
  <input id="mdp" type="password" autocomplete="new-password" minlength="8" required
    style="width:100%;min-height:56px;padding:0 16px;border-radius:16px;border:1px solid var(--dim);background:var(--surface);color:var(--chalk);font:inherit">
  <p id="msg" role="status" aria-live="polite" class="muted" style="min-height:1.6em;margin:12px 0"></p>
  <button class="btn primary" type="submit" style="width:100%;justify-content:center;border:0">Enregistrer</button>
</form>
</div></article>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.min.js"></script>
<script>
(function () {
  var msg = document.getElementById('msg'), f = document.getElementById('f');
  function dire(t, erreur) { msg.textContent = t; msg.style.color = erreur ? 'var(--flare)' : 'var(--mineral)'; }
  var client = supabase.createClient('https://oyyoajcfwcirvpuszhbb.supabase.co',
    'sb_publishable_O_bWbG8NCXR_03unPUk17g_slixbz-P');
  // Le lien de l'e-mail ouvre cette page avec un jeton temporaire : sans lui,
  // rien a faire ici.
  var pret = false;
  client.auth.onAuthStateChange(function (evenement, session) { if (session) pret = true; });
  client.auth.getSession().then(function (r) {
    if (r.data && r.data.session) pret = true;
    if (!pret && location.hash.indexOf('access_token') < 0) {
      f.hidden = true;
      dire("Ce lien n'est plus valide. Redemande un e-mail depuis l'application : Profil, Compte en ligne, Mot de passe oublié.", true);
    }
  });
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var mdp = document.getElementById('mdp').value;
    if (mdp.length < 8) { dire('Au moins 8 caractères.', true); return; }
    dire('Enregistrement...');
    client.auth.updateUser({ password: mdp }).then(function (r) {
      if (r.error) { dire("Impossible d'enregistrer. Le lien a peut-être expiré, redemande un e-mail depuis l'application.", true); return; }
      f.hidden = true;
      document.getElementById('intro').textContent = '';
      dire("C'est fait. Retourne dans l'application et connecte toi avec ton nouveau mot de passe.");
      client.auth.signOut();
    });
  });
})();
</script>
""")
print("pages ecrites")
