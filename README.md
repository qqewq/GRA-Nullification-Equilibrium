https://orcid.org/my-orcid?orcid=0009-0004-1872-1153
https://doi.org/10.5281/zenodo.20846641
-----------
# GRA Nullification Equilibrium / Равновесие обнуления GRA

[English](#english) | [Русский](#русский)

---

## English

**GRA Nullification Equilibrium** is a reference implementation of the chiral nullification / foam generation dynamics described in the GRA ecosystem.  
It provides:
- Mathematical core (Python) for computing foam Φ, hierarchical stability, chiral mapping, and nullification operator.
- REST API (FastAPI) to run simulations.
- Interactive frontend for real‑time visualisation of foam evolution and equilibrium.
- Formal verification and test suite.
- Bilingual paper with derivations.

### Quick Start

```bash
git clone https://github.com/qqewq/GRA-Nullification-Equilibrium
cd GRA-Nullification-Equilibrium
pip install -r backend/requirements.txt
uvicorn backend.app:app --reload
```

Then open `frontend/index.html` in a browser.

### Core Concepts

- **Foam** Φ(π, w, s) – measure of contradiction / entropy.
- **Nullification operator** 𝒩(π, w, s) → (π', 0, 0), where π' = (R, L) is a chiral pair.
- **Chiral mapping** R ↔ L via reflection operator Z.
- **Hierarchical stability** rank N = min{n | ∂ⁿΦ/∂kⁿ = 0}.
- **Wave nullification** ψ(k) = exp(−λ Φ(k)).
- **Equilibrium** – balance between foam nullification and generation, governed by the N‑th derivative criterion.

### Verification

Run verification scripts:
```bash
python verification/verify_nullification.py
python verification/verify_chiral_balance.py
```

Run tests:
```bash
pytest tests/
```

### License

MIT © qqewq

---

## Русский

**GRA Равновесие обнуления** — эталонная реализация хиральной динамики обнуления/генерации пены, описанной в экосистеме GRA.

Предоставляет:
- Математическое ядро (Python) для вычисления пены Φ, иерархической стабильности, хирального отображения и оператора обнуления.
- REST API (FastAPI) для запуска симуляций.
- Интерактивный фронтенд для визуализации эволюции пены и равновесия в реальном времени.
- Формальную верификацию и набор тестов.
- Билингвальную статью с выводами.

### Быстрый старт

```bash
git clone https://github.com/qqewq/GRA-Nullification-Equilibrium
cd GRA-Nullification-Equilibrium
pip install -r backend/requirements.txt
uvicorn backend.app:app --reload
```

Затем откройте `frontend/index.html` в браузере.

### Основные понятия

- **Пена** Φ(π, w, s) – мера противоречия / энтропии.
- **Оператор обнуления** 𝒩(π, w, s) → (π', 0, 0), где π' = (R, L) – хиральная пара.
- **Хиральное отображение** R ↔ L через оператор отражения Z.
- **Иерархическая стабильность** ранг N = min{n | ∂ⁿΦ/∂kⁿ = 0}.
- **Волновая обнулёнка** ψ(k) = exp(−λ Φ(k)).
- **Равновесие** – баланс между обнулением и генерацией пены, управляемый критерием N‑й производной.

### Верификация

Запустите скрипты верификации:
```bash
python verification/verify_nullification.py
python verification/verify_chiral_balance.py
```

Запустите тесты:
```bash
pytest tests/
```

### Лицензия

MIT © qqewq
