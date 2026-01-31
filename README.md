# PyLL - Todo Application

Flask 기반의 간단한 Todo 애플리케이션입니다. PostgreSQL 데이터베이스와 Redis 캐시를 사용하여 Todo 항목을 관리합니다.

## 기능

- ✓ Todo 항목 추가
- ✓ Todo 항목 완료/미완료 토글
- ✓ 모든 Todo 항목 조회
- ✓ PostgreSQL을 사용한 데이터 영구 저장
- ✓ Redis를 사용한 캐싱

## 프로젝트 구조

```
pyll/
├── app.py                 # Flask 애플리케이션
├── requirements.txt       # Python 의존성
├── Dockerfile            # Docker 이미지 설정
├── docker-compose.yml    # Docker Compose 설정
├── README.md            # 이 파일
├── data/                # 데이터 디렉토리
├── scripts/
│   └── deploy-pyll.sh   # 배포 스크립트
└── templates/
    └── index.html       # 메인 화면 템플릿
```

## 설치 및 실행

### 필수 요구사항

- Docker & Docker Compose
- 또는 Python 3.9+, PostgreSQL, Redis

### Docker Compose로 실행 (권장)

```bash
docker-compose up --build
```

애플리케이션은 http://localhost:5000 에서 접근할 수 있습니다.

### 로컬 환경에서 실행

1. 의존성 설치:

```bash
pip install -r requirements.txt
```

2. 환경 변수 설정:

```bash
export DATABASE_URL=postgresql://user:password@localhost:5432/pyll_db
export FLASK_APP=app.py
```

3. 데이터베이스 초기화:

```bash
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
```

4. 애플리케이션 실행:

```bash
python app.py
```

## 기술 스택

- **Backend**: Flask
- **Database**: PostgreSQL
- **Cache**: Redis
- **ORM**: SQLAlchemy
- **Frontend**: HTML/CSS/JavaScript
- **Containerization**: Docker

## 환경 변수

- `DATABASE_URL`: PostgreSQL 연결 문자열
- `FLASK_ENV`: Flask 환경 (development/production)
- Redis는 docker-compose에서 자동으로 설정됩니다.

## API 엔드포인트

| 메서드 | 엔드포인트 | 설명 |
|--------|-----------|------|
| GET | `/` | 모든 Todo 항목 조회 |
| POST | `/add` | 새로운 Todo 항목 추가 |
| GET | `/update/<id>` | Todo 항목 완료 상태 토글 |

## 배포

```bash
chmod +x scripts/deploy-pyll.sh
./scripts/deploy-pyll.sh
```

## 라이선스

MIT License

