---
description: API Structure
globs: *
alwaysApply: true
---
以下は、APIの開発のおいて、役割ごとに整理されています。

### 1. **ディレクトリ構造の基本方針**
- **機能ごとの分割**: 各機能は独立したディレクトリに分割されている。
- **責務の分離**: Entity、UseCase、InterfaceAdapterを明確に分離し、機能をシンプルに保ちます。
- **共通化可能な処理の抽出**: 複数の場所で使用される共通処理は、`utils`ディレクトリに配置し再利用性を高める。

### 2. **各レイヤーの構成**　※`src`配下
- **entity**: `entities`ディレクトリに格納する。(例: `user_entity.py`, `item_entity.py`)
- **repository**: `repositories`ディレクトリに格納する。
    - **implements**: `impls`ディレクトリに格納する。(例: `user_repository.py`, `item_repository.py`)
    - **interface**: `interfaces`ディレクトリに格納する。(例: `user_interface.py`, `item_interface.py`)
- **routes**: `routes`ディレクトリに格納する。
    - **api**: `api`ディレクトリに格納する。
        - **v~**: `v~`ディレクトリに格納する。(例: `v1`, `v2`)
            - **endpoint**: `{機能名}`ディレクトリに格納する。(例: `accounts`, `items`)
                - **request**: `requests`ディレクトリに格納する。`{機能名}`で使用する、InputDataを格納する。
                - **response**: `responses`ディレクトリに格納する。`{機能名}`で使用する、OutputDataを格納する。
                - **__init__.py**: `endpoint`のプレフィックスを付与するために各エンドポイントを収集する。
            - **__init__.py**: `v~`のプレフィックスを付与するために各エンドポイントを収集する。
- **service**: `services`ディレクトリに格納する。(例: `accounts_service.py`, `items_service.py`)
- **configs**: `configs`ディレクトリに格納する。
    - **.env_{stage}**: 各環境における設定ファイルを配置する。
    - **__init__.py**: `__init__`関数で環境別の読み込みに対応する。

### 3. **共通ディレクトリ**
- **utils**: `utils`ディレクトリに格納する。
    - **機能**: `{機能}`ディレクトリに格納する。(例: `convert_date`)
        - **repository**: `repositories`ディレクトリに格納する。
            - **implements**: `impls`ディレクトリに格納する。
            - **interfaces**: `interfaces`ディレクトリに格納する。
        - **__init__.py**: serviceとして動作する。
        - **modules.py**: Injectorを使用して、依存関係を解決する。
- **tests**: `tests`ディレクトリに格納する。
