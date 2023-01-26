function solution(today, terms, privacies) {
  var answer = [];
  today = parseInt(today.replaceAll(".", ""), 10);
  const map = new Map();
  const processedPeriodList = [];

  terms.forEach((termElement) => {
    const [term, period] = termElement.split(" ");
    map.set(term, parseInt(period, 10));
  });

  privacies.forEach((privaciyElement) => {
    let [date, terms] = privaciyElement.split(" ");
    let [originalYear, originalMonth, originalDate] = date.split(".");
    originalYear = parseInt(originalYear, 10);
    originalMonth = parseInt(originalMonth, 10);
    originalDate = parseInt(originalDate, 10);

    const termsPreriod = map.get(terms);
    let afterYear = Math.floor((termsPreriod + originalMonth) / 12);
    let afterMonth = (termsPreriod + originalMonth) % 12;

    if (afterMonth === 0) {
      afterYear -= 1;
      afterMonth = 12;
    }

    const processedPeriod =
      (originalYear + afterYear) * 10000 + afterMonth * 100 + originalDate;
    processedPeriodList.push(processedPeriod);
  });

  processedPeriodList.forEach((period, index) => {
    if (today >= period) {
      answer.push(index + 1);
    }
  });

  return answer;
}

console.log(
  solution(
    "2020.01.01",
    ["Z 12", "D 5"],
    [
      "2019.01.01 D",
      "2019.11.15 Z",
      "2019.08.02 D",
      "2019.07.01 D",
      "2018.12.28 Z",
    ]
  )
);
