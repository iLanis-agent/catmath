// Cat Math engine - litter box count, litter pounds and depth honesty.
// Every norm is a labeled care norm; the app never gives a health verdict.

function assertPositive(value, label) {
  if (!Number.isFinite(value) || value <= 0) {
    throw new Error(label + " must be above zero");
  }
}

function tenths(x) {
  return Math.floor(x * 10 + 0.5) / 10;
}

function fixed1(x) {
  return tenths(x).toFixed(1);
}

// Labeled care norm: one litter box per cat, plus one.
function boxTruth(cats) {
  assertPositive(cats, "the cat count");
  const boxes = cats + 1;
  const catWord = cats === 1 ? "cat" : "cats";
  const boxWord = boxes === 1 ? "box" : "boxes";
  const verb = cats === 1 ? "asks" : "ask";
  return cats + " " + catWord + " " + verb + " " + boxes + " litter " + boxWord + " honestly.";
}

// Labeled care norm: about 20 pounds of clumping litter per cat per month.
function litterTruth(cats) {
  assertPositive(cats, "the cat count");
  const pounds = tenths(cats * 20);
  const bags = tenths(pounds / 40);
  const catWord = cats === 1 ? "cat goes" : "cats go";
  return cats + " " + catWord + " through " + fixed1(pounds) + " pounds a month, " +
    fixed1(bags) + " of a 40-pound bag honestly.";
}

// Labeled care norm: keep the litter 2 to 3 inches deep.
function depthTruth(inches) {
  assertPositive(inches, "the depth");
  const d = tenths(inches);
  let band;
  if (d < 2) {
    band = "too shallow to bury, and the smells win";
  } else if (d <= 3) {
    band = "right in the sweet spot";
  } else {
    band = "deep enough to waste and track";
  }
  return fixed1(d) + " inches of litter reads " + band + " honestly.";
}

if (typeof module !== "undefined") {
  module.exports = { boxTruth, litterTruth, depthTruth, tenths, fixed1 };
}
