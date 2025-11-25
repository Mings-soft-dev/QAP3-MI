// Desc:Invoice generator for lawn care services
// Author:Morgan Ings
// Dates:Nov 18 2025


var $ = function (id) {
  return document.getElementById(id);
};


// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

// Get user input.
let CusName = prompt("Enter Customer's Name: ");
let PhoneNum = prompt("Enter Phone Number: ");
let StAddr = prompt("Enter Street Address: ");
let City = prompt("Enter City: ");
let SquareFeet = prompt("Enter Square Feet of Lawn: ");
SquareFeet = parseFloat(SquareFeet);

// Define program constants.
const BorderRate = 0.28;//per SQ FT
const TaxRate = 0.15;
const MoeRate = 0.04;//per SQ FT at 95% of remaining lawn
const FertilizerRate = 0.03;//per SQ FT
const EnvironmentTaxRate = 0.014;//of total charges

// calculate costs
let BorderCost = (SquareFeet * 0.04) * BorderRate;
BorderCost = parseFloat(BorderCost);

let MoeCost = (SquareFeet * 0.95) * MoeRate;
MoeCost = parseFloat(MoeCost);

let FertilizerCost = SquareFeet * FertilizerRate;
FertilizerCost = parseFloat(FertilizerCost);

let TotalCharges = BorderCost + MoeCost + FertilizerCost;
TotalCharges = parseFloat(TotalCharges);

let SalesTax = TotalCharges * TaxRate;
SalesTax = parseFloat(SalesTax);

let EnvironmentTax = TotalCharges * EnvironmentTaxRate;
EnvironmentTax = parseFloat(EnvironmentTax);

let InvoiceTotal = TotalCharges + SalesTax + EnvironmentTax;
InvoiceTotal = parseFloat(InvoiceTotal);

// format outputs
let BorderCostDsp = cur2Format.format(BorderCost);
let MoeCostDsp = cur2Format.format(MoeCost);
let FertilizerCostDsp = cur2Format.format(FertilizerCost);
let TotalChargesDsp = cur2Format.format(TotalCharges);
let SalesTaxDsp = cur2Format.format(SalesTax);
let EnvironmentTaxDsp = cur2Format.format(EnvironmentTax);
let InvoiceTotalDsp = cur2Format.format(InvoiceTotal);

// outputs
document.writeln("<br/><br/>");
document.writeln("<table class='invoiceTable'>");

document.writeln("<tr>");
document.writeln("<th colspan='2' class='centertext'>Mo's LawnCare Services - Customer Invoice</th>");
document.writeln("</tr>");


document.writeln("<tr>");
document.writeln("<td colspan='2'>Customer Details: <br/><br/>" + CusName + ", " + PhoneNum + ", <br/>" + StAddr + ", " +City + "<br/><br/>Property size (in sq ft): " + SquareFeet + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Border cost: </td>");
document.writeln("<td class='righttext'>" + BorderCostDsp + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Mowing cost: </td>");
document.writeln("<td class='righttext'>" + MoeCostDsp + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Fertilizer cost: </td>");
document.writeln("<td class='righttext'>" + FertilizerCostDsp + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br/></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Total charges: </td>");
document.writeln("<td class='righttext'>" + TotalChargesDsp + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br/></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Sales tax(HST): </td>");
document.writeln("<td class='righttext'>" + SalesTaxDsp + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Environment tax: </td>");
document.writeln("<td class='righttext'>" + EnvironmentTaxDsp + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br/></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Invoice total: </td>");
document.writeln("<td class='righttext'>" + InvoiceTotalDsp + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<th colspan='2' class='centertext'>Turning Lawns into Landscapes</th>");
document.writeln("</tr>");

document.writeln("</table>");


/*
document.writeIn("<th>Lawn Care Service Invoice</th>");

document.writeIn("<tr>Customer Name: " + CusName + "</tr>");
document.writeIn("<tr>Phone Number: " + PhoneNum + "</tr>");
document.writeIn("<tr>Street Address: " + StAddr + "</tr>");
document.writeIn("<tr>City: " + City + "</tr>");
*/
