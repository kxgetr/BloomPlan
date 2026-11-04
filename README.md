# BloomPlan

Hedef yanlış pozitif olasılığına göre Bloom filtre boyutu ve hash sayısı önerir.

## Girdi

items ve probability (0 ile 1 arasında).

## Kullanım

Python 3.11+, standart kütüphane.

```sh
python bloomplan.py input.json
python verify.py
```

Dosya verilmezse stdin okunur. Sonuç stdout üzerinde JSON olarak yazılır. Girdi hatası çıkış kodu 2 üretir.

Örnek sonuç:

```json
{
  "bits": 959,
  "hashes": 7
}
```
