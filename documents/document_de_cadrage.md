## Document de Cadrage – Projet : Coach IA pour l'Analyse de Setups ICT via Screenshots

### 1. Mission et vision
- **Analyse pré-trade** : Fournir aux traders une analyse assistée par IA des configurations potentielles du marché basées sur les concepts ICT, avant la prise de position.
- **Support à la décision** : Utiliser l'IA pour identifier la conformité des structures de marché (visibles sur les screenshots) avec des checklists ICT prédéfinies (Continuation, Reversal).
- **Coaching contextuel** : Offrir un feedback sur les setups potentiels, soulignant les points forts et les faiblesses par rapport aux critères ICT, pour améliorer la reconnaissance des patterns.
- **Horizon** : Développer un outil d'aide à la décision rapide et visuel pour renforcer la discipline dans l'application des stratégies ICT.

### 2. Objectifs et KPIs
- **Objectifs clés** :
  - Identifier correctement les setups ICT potentiels (Continuation/Reversal) à partir des screenshots multi-timeframe fournis.
  - Évaluer la conformité des screenshots aux checklists ICT correspondantes.
  - Fournir un feedback clair et exploitable sur les setups identifiés.
- **KPIs et granularité** :
  - **Précision de l'identification des setups** (taux de setups valides correctement identifiés par l'IA).
  - **Pertinence du feedback** (évaluée qualitativement par l'utilisateur).
  - **Taux de conformité checklist** (pourcentage de critères de la checklist identifiés correctement par l'IA sur les images).
- **Périodes de suivi** : Analyse par session d'utilisation.

### 3. Architecture technique (haut niveau)
1.  **Front‑end (Local)**
    - Application web interactive développée avec Streamlit, exécutée localement.
    - Widgets pour : upload multiple de fichiers images (screenshots), sélection des timeframes associées, bouton de déclenchement de l'analyse, affichage des images et du feedback IA.
2.  **Traitement des Images (Local)**
    - Les images uploadées sont encodées en Base64 directement dans l'application Streamlit avant d'être envoyées à l'API OpenAI.
    - **Supabase Storage/Database :** Non utilisés dans la V1 pour le stockage des images ou des données d'analyse, afin de simplifier l'architecture initiale. Pourraient être ajoutés ultérieurement si une persistance est nécessaire.
    - **Authentification :** Non requise pour une V1 purement locale/analytique sans persistance de données utilisateur long terme.
3.  **Moteur IA / Analyse Visuelle (OpenAI)**
    - **Objectif :** Analyser un set de screenshots de graphiques (multi-timeframe) pour identifier et évaluer des setups ICT.
    - **Inputs Clés pour l'IA :**
        - **Images (Encodées en Base64) :** Issues des fichiers uploadés par l'utilisateur via Streamlit.
        - **Timeframes associées :** Spécifiées par l'utilisateur pour chaque image (ex: D, 4H, 1H, 15M).
        - **Checklists ICT :** Définitions structurées des critères pour les setups (Continuation/Reversal), stockées localement (fichier config/Python `utils/ict_checklists.py`). Servent de guide pour le prompt de l'IA.
    - **Pipeline d'Analyse IA (via API OpenAI `openai` - Modèle Vision `gpt-4o`) :**
        1. **Prise en compte Multi-Timeframe :** L'IA reçoit l'ensemble des images (Base64) et leurs timeframes.
        2. **Analyse Visuelle ICT :** Le modèle analyse les éléments graphiques (structure de marché, liquidité, FVG, OB, etc.) sur les images en fonction des concepts ICT et des checklists fournies dans le prompt.
        3. **Génération de Feedback :** Production d'un rapport textuel identifiant les setups potentiels, évaluant leur conformité à la checklist correspondante, et fournissant un coaching/des points d'attention.
4.  **Sécurité & conformité**
    - Gestion sécurisée de la clé API OpenAI (via variables d'environnement / `.env`). Pas de stockage de données utilisateur sensibles dans la V1.

### 4. Sources de Données Utilisateur
- **Upload de Screenshots :** Fichiers images (ex: PNG, JPG) représentant les graphiques du marché sur différentes unités de temps, uploadés par l'utilisateur via l'interface Streamlit.
- **Sélection de Timeframe :** Association manuelle d'une unité de temps (D, 4H, 1H, 15M, etc.) à chaque screenshot uploadé.

**Prochaines étapes** :
- Suivre la `revised_todo_list.md` pour l'implémentation.
- Commencer par l'initialisation de la structure du projet et des dépendances.
