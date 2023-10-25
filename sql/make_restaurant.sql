CREATE TABLE restaurant (
    id SERIAL PRIMARY KEY, -- 自動生成される連番の主キー
    name VARCHAR(255) NOT NULL, -- VARCHAR型の名前列、NULL値を許容しない
    genre VARCHAR(255), -- VARCHAR型のジャンル列
    main VARCHAR(255), -- VARCHAR型のメイン料理列
    price_range VARCHAR(50), -- VARCHAR型の価格帯列
    longitude DOUBLE PRECISION NOT NULL, -- DOUBLE PRECISION型の経度列、NULL値を許容しない
    latitude DOUBLE PRECISION NOT NULL, -- DOUBLE PRECISION型の緯度列、NULL値を許容しない
    comment TEXT -- テキスト型のコメント列
);