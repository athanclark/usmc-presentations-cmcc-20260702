---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
style: |
  section {
    font-size: 22px;
    line-height: 1.22;
    padding: 44px 70px;
  }
  section.lead {
    font-size: 24px;
  }
  section h1 {
    font-size: 1.65em;
    line-height: 1.08;
    margin: 0 0 0.35em 0;
  }
  section h2 {
    font-size: 1.25em;
    line-height: 1.12;
    margin: 0.25em 0 0.5em 0;
  }
  section p,
  section ul,
  section ol,
  section blockquote,
  section table {
    margin-top: 0.45em;
    margin-bottom: 0.45em;
  }
  section li {
    margin-top: 0.16em;
    margin-bottom: 0.16em;
  }
  section table {
    font-size: 0.82em;
  }
  section sup {
    font-size: 0.65em;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .stretch img {
    width: 100em;
  }
  .tiny {
    font-size: 12px;
    line-height: 1.15;
    word-break: break-word;
  }
  .tiny h1 {
    font-size: 1.45em;
  }
  .tiny p {
    margin-top: 0.35em;
    margin-bottom: 0.35em;
  }
---

![bg left:40% 80%](./3nb.png)

# CMCC Duties and Responsibilities for SIPR Assets

## Custody, Couriering, Imaging, and Return Procedures

**Audience:** Marines and staff who may receive, move, image, store, or return classified SIPR assets.

**Training outcome:** understand the vocabulary, records, custody standards, courier requirements, and end-to-end process for temporary unit-to-unit transfer of SIPR assets.

---

# 1. Scope and Ground Rules

This deck provides a **policy-level SOP model** for SIPR laptops, hard drives, removable media, and related classified/COMSEC material.

It does **not** replace:

- Local Command Security Manager direction.
- COMSEC Manager/KMI Operating Account guidance.
- SCI/SAP-specific rules.
- Local vault/open-storage approval documentation.

When local policy is stricter than this deck, use the stricter rule.

**Security consequence:** treating local procedures as optional can turn a minor administrative mistake into an accountability failure.

---

# 2. Classified Information vs. Classified Material

**Classified information** is national-security information marked Confidential, Secret, or Top Secret.

**Classified material** is the physical or digital object that contains, stores, records, or embeds classified information.

Examples:

- SIPR laptop.
- Classified hard drive or solid-state drive.
- Removable media.
- Printed document.
- COMSEC keying material or equipment.

Marine Corps policy treats classified National Security Information as including any matter, document, product, substance, or item of equipment on or in which classified information is recorded or embedded.<sup><a href="#ref-1">[1]</a></sup>

**Security consequence:** if a laptop chassis is tracked but the classified drive is not, the command may lose accountability for the actual classified material.

---

# 3. What Is a CMCC?

A **Classified Material Control Center (CMCC)** is a local command control function for receiving, logging, storing, issuing, inventorying, and returning classified material.

Marine Corps policy lists CMCC programs as a best practice for classified-material control, including document-control and secondary-control-point functions.<sup><a href="#ref-2">[2]</a></sup>

**Plain meaning:** the CMCC is the place or function that answers, “Who has this classified item, where is it, and what record proves it?”

**Security consequence:** without a CMCC-style control point, classified assets can move by habit, email, or word of mouth instead of by accountable custody.

---

# 4. What Is COMSEC?

**Communications Security (COMSEC)** protects communications from exploitation and ensures authenticity.

COMSEC includes:

- Cryptographic security.
- Transmission security.
- Emissions security.
- Physical security of COMSEC material and information.<sup><a href="#ref-3">[3]</a></sup>

**COMSEC material** includes items designed to secure or authenticate telecommunications, including key, equipment, modules, devices, documents, hardware, firmware, or software that embody cryptographic logic or perform COMSEC functions.<sup><a href="#ref-4">[4]</a></sup>

**Security consequence:** mishandling COMSEC material may be more serious than ordinary property loss because it can affect cryptographic trust and mission communications.

---

# 5. What Are CMCS, KMI, and KOA?

The **COMSEC Material Control System (CMCS)** is the logistics and accounting system used to distribute, control, and safeguard COMSEC material marked CRYPTO; EKMS and KMI are examples of tools used by CMCS.<sup><a href="#ref-5">[5]</a></sup>

**Key Management Infrastructure (KMI)** provides generation, production, storage, protection, distribution, control, tracking, and destruction for cryptographic keying material.<sup><a href="#ref-6">[6]</a></sup>

A **KMI Operating Account (KOA)** is the KMI account relationship used to manage devices and control distribution of KMI products to those devices.<sup><a href="#ref-7">[7]</a></sup>

**Security consequence:** using a property receipt alone for COMSEC/KMI material may fail to meet COMSEC accountability requirements.

---

# 6. What Is CCI?

A **Controlled Cryptographic Item (CCI)** is normally unclassified equipment or a cryptographic component handled through the COMSEC Material Control System, an equivalent control system, or both.<sup><a href="#ref-8">[8]</a></sup>

**Important distinction:** CCI may be unclassified by itself, but it is still controlled.

Examples may include approved cryptographic devices, components, or modules that perform a COMSEC function.

**Security consequence:** treating CCI as ordinary IT gear can create a COMSEC incident even when the item is not marked classified.

---

# 7. What Are SF-153, SD-572, CBAR, and CBAP?

**SF-153** is the COMSEC Material Report. It may support transfer, inventory, destruction, hand-receipt, or other COMSEC material reporting actions.<sup><a href="#ref-9">[9]</a></sup>

**SD-572** is the Cryptographic Access Certification and Termination form used to certify and terminate access to U.S. classified cryptographic information.<sup><a href="#ref-10">[10]</a></sup>

**CBAR/CBAP:** these terms appear to be local or command-specific validation artifacts rather than publicly verified DoD-wide form names. Treat them as local access/briefing/authorization records until your COMSEC Manager or Security Manager confirms the correct form name and authority.

**Security consequence:** using the wrong validation document may mean the recipient was never properly authorized to receive or access the material.

---

# 8. Policy Baseline

Classified material must be protected by one of two conditions:

1. Stored as required by policy.
2. Under the personal observation and control of an authorized person.<sup><a href="#ref-11">[11]</a></sup>

Before access is granted, the person must have:

- Proper clearance eligibility.
- SF-312 on file.
- Need-to-know.
- Any additional COMSEC, cryptographic, NATO, SCI, SAP, or local briefing required for the material.<sup><a href="#ref-12">[12]</a></sup>

**Security consequence:** custody without authorization is not just poor paperwork; it can be unauthorized disclosure.

---

# 9. Who May Sign for Classified SIPR Assets?

Qualified signers should be appointed or otherwise documented by the command.

Typical qualified signers include:

- Command Security Manager or alternate.
- CMCC custodian or alternate.
- COMSEC Manager, KOA Manager, or alternate, when COMSEC/KMI material is involved.
- Formally appointed hand-receipt holder or lab custodian.

Do **not** let an ordinary end user sign merely because they are the technical point of contact.

**Security consequence:** release to an unqualified signer is at least an accountability failure and may become a compromise if access was not authorized.

---

# 10. How to Validate a Recipient Before Release

Before releasing the asset, validate:

1. Identity: CAC/DoD ID and unit affiliation.
2. Eligibility: clearance level and access record.
3. Need-to-know: mission requirement for that asset.
4. Appointment: courier letter/card, access roster, CMCC appointment, COMSEC appointment, or lab-custodian designation.
5. Special access: SD-572 or local COMSEC/KMI validation when classified cryptographic information is involved.<sup><a href="#ref-13">[13]</a></sup>

For classified cryptographic information, SD-572 Section I must be executed before access, and Section II must be executed when access is no longer required.<sup><a href="#ref-14">[14]</a></sup>

**Security consequence:** if qualification is assumed instead of validated, the release may become a security violation or compromise.

---

# 11. Core Custody Records

Use the record required by the material type:

| Material type | Minimum record |
|---|---|
| Ordinary classified SIPR asset | CMCC log and local hand receipt |
| Classified hard drive/media | CMCC/media log and hand receipt |
| COMSEC material | SF-153 or COMSEC-account-directed record |
| Classified cryptographic information access | SD-572 and access briefing/debriefing record |
| Property accountability | Property record, GCSS-MC/DPAS/local equivalent |

The custody record should identify the item without adding unnecessary classified operational detail.

**Security consequence:** a property record may prove ownership, but it does not automatically prove classified custody.

---

# 12. Temporary Hand Receipts

A temporary hand receipt should record:

- Releasing unit and accepting unit.
- Releasing official, receiving official, and witness when required.
- Courier name and courier authorization reference.
- Chassis serial number and property tag.
- Hard-drive or storage-media serial numbers.
- Classification level and control caveats.
- Exact purpose, date/time, expected return, and temporary storage location.

Material removed from an approved open-storage area must be controlled and accounted for until returned.<sup><a href="#ref-15">[15]</a></sup>

**Security consequence:** incomplete hand receipts make it difficult to determine last known location, responsible person, and whether a loss occurred.

---

# 13. Serial Number Validation

Validate both:

1. **Chassis serial/property tag** for the laptop or workstation.
2. **Drive/media serials** for internal drives, removable drives, SSDs, and other classified storage media.

Marine Corps policy specifically includes removable or removed classified hard drives, external hard drives, computers, disks, documents, and other media within classified control measures.<sup><a href="#ref-16">[16]</a></sup>

**Best practice:** record drive serials at release, intake, before imaging, after imaging, before return, and at final receipt.

**Security consequence:** a missing or swapped hard drive is potentially a loss of classified material, even if the laptop chassis is present.

---

# 14. Courier Requirements

For this SOP, a courier package should include:

- Courier appointment letter.
- Issued courier card or DD Form 2501 if used locally.
- DoD ID and government photo ID.
- Copy of inventory or hand receipt retained by courier.
- Office-retained copy of inventory or hand receipt.
- Locked, opaque, durable container such as an approved Pelican-style case.
- Inner sealed package or administrative packet as locally required.

DoD policy requires written authorization for persons approved to escort, courier, or hand-carry classified material, and that authorization may be a letter, courier card, travel orders, or other written document.<sup><a href="#ref-17">[17]</a></sup>

**Security consequence:** couriering without documented authorization is an infraction at minimum; loss of custody can become a violation or compromise.

---

# 15. Packaging and Pelican Case Standards

DoD policy requires classified material being transferred to be enclosed in two opaque, sealed envelopes, wrappings, or containers durable enough to protect against exposure and show tampering.<sup><a href="#ref-18">[18]</a></sup>

For hand-carry outside an activity, a locked briefcase or zippered pouch may serve as the outer wrapper; a locally approved locked Pelican-style case can serve the same practical purpose if approved by the Security Manager and compatible with local policy.<sup><a href="#ref-19">[19]</a></sup>

Do not mark the outside of the container in a way that reveals or advertises classified contents.<sup><a href="#ref-20">[20]</a></sup>

**Security consequence:** poor packaging can create accidental exposure, tampering uncertainty, or unauthorized disclosure.

---

# 16. Government Vehicle vs. POV

**Preferred method:** government vehicle with official routing and direct travel.

**POV use:** only when authorized by the command or Security Manager and when the courier can maintain continuous personal custody.

Courier rules apply regardless of vehicle:

- Do not leave the material unattended.
- Do not make unauthorized stops.
- Do not open the package en route except under policy-defined circumstances.
- Arrange approved secure storage if travel is interrupted or overnight storage becomes necessary.<sup><a href="#ref-21">[21]</a></sup>

**Security consequence:** leaving classified material in a POV, even briefly, may be a reportable security violation and may become a loss or compromise.

---

# 17. Acceptance at the Receiving Unit

The receiving unit should sign only after completing a physical sighting.

Acceptance should include:

1. Validate courier identity and courier authority.
2. Compare hand receipt/SF-153 to the physical asset.
3. Verify chassis serial and drive/media serials.
4. Inspect seals, locks, and packaging for tampering.
5. Record date/time, location, receiving official, and witness if required.
6. Refuse or annotate discrepancies before signing.

**Security consequence:** signing before verification creates false custody and may conceal loss, tampering, or unauthorized substitution.

---

# 18. How the Hand Receipt Enters Inventory

The owning unit should annotate its inventory as:

> “Issued on temporary hand receipt to [unit] for [purpose], [date/time], expected return [date/time].”

The receiving unit should enter the asset into a temporary custody log with:

- Owning unit.
- Receiving custodian.
- Room or container location.
- Authorized movement locations.
- Work status.
- Return status.

Marine Corps policy encourages logs for hard-copy classified information and requires control and accountability when material leaves open storage.<sup><a href="#ref-22">[22]</a></sup>

**Security consequence:** if neither unit inventory reflects temporary custody, the asset is effectively uncontrolled.

---

# 19. Inventory Frequency and Physical Validation

Minimum inventory expectations vary by material type and classification.

For Top Secret material, Marine Corps policy requires inventories at least annually or more often when circumstances warrant.<sup><a href="#ref-23">[23]</a></sup>

For Secret and below, material inside approved open storage requires no additional control while it remains there, but material removed from open storage must be controlled and accounted for until returned.<sup><a href="#ref-24">[24]</a></sup>

For temporary customer assets, use a stricter local standard:

- 100% physical validation at intake.
- 100% physical validation before and after imaging.
- 100% physical validation before return.
- 100% reconciliation during custodian change, discrepancy, or suspected compromise.

**Security consequence:** delayed inventory can delay discovery of loss and increase damage assessment scope.

---

# 20. Scenario: Customer Unit Prepares Asset for 3NB Imaging

For this deck, **3NB** refers to the receiving/imaging unit or CMCC function performing the SIPR imaging work.

The customer unit should:

1. Contact its Security Manager, CMCC, vault custodian, or COMSEC Manager as applicable.
2. Retrieve the SIPR asset from approved storage.
3. Validate chassis and drive/media serials.
4. Prepare the hand receipt, SF-153 if COMSEC material is involved, and courier packet.
5. Appoint or validate the courier.
6. Package the asset in the approved locked case.
7. Retain a complete copy of the transfer packet.

The asset should not be released directly from an end user or help desk without CMCC/security accountability.

**Security consequence:** bypassing CMCC creates a custody gap before the asset ever reaches 3NB.

---

# 21. Scenario: 3NB Receives the Asset

At 3NB, the asset should be received by one of the following:

- 3NB CMCC custodian or alternate.
- Command Security Manager or alternate.
- COMSEC/KOA Manager or alternate when COMSEC/KMI applies.
- Formally appointed SIPR imaging lab custodian.

The 3NB receiver should:

1. Verify courier authority.
2. Inspect package condition.
3. Validate all recorded serial numbers.
4. Sign receipt only after physical validation.
5. Enter the item into the 3NB temporary classified-material custody log.
6. Store the complete packet with the CMCC record, not just in the technician’s notes.

**Security consequence:** if a technician signs without appointment, the record may not establish valid transfer of custody.

---

# 22. Scenario: Imaging Lab Storage

A SIPR imaging lab may store assets only if the room is approved for the classification level and storage method.

If the room is **not** approved open storage, assets should be stored in a GSA-approved container, vault, or other approved storage when not under direct observation and control of an authorized person.<sup><a href="#ref-25">[25]</a></sup>

An X.509/CAC/electronic lock helps control access, but DoD policy warns that electrically actuated locks do not, by themselves, substitute for required classified-storage locks or standards.<sup><a href="#ref-26">[26]</a></sup>

**Security consequence:** an electronically controlled room that is not approved storage can still be improper classified storage.

---

# 23. Scenario: Recording Location Inside 3NB

The customer-to-3NB hand receipt should identify the receiving unit and authorized purpose.

The 3NB internal custody log should record the most precise controlled location practical, such as:

- Building.
- Room number.
- Vault/container number.
- Imaging bench or cage identifier if locally used.
- Date/time of internal movement.
- Person moving the asset and witness if required.

**Recommended wording:** the customer receipt may state “3NB CMCC/SIPR imaging lab, approved storage locations only,” while the 3NB custody log records exact room/container movement.

**Security consequence:** building-only tracking may be insufficient if the asset cannot be immediately located during inventory.

---

# 24. Scenario: Moving Customer Assets Between Rooms

Moving a customer asset between rooms should require:

1. Authorized person moving the asset.
2. Continuous custody or proper packaging.
3. Update to internal custody log.
4. Witness or two-person integrity (TPI) when required by material type or local SOP.
5. Storage only in approved rooms or containers.

A new customer hand receipt is not required for every internal room move if 3NB remains the accountable temporary custodian and the internal movement log is complete.

**Security consequence:** unlogged internal movement can look identical to loss during an audit.

---

# 25. Scenario: Imaging Complete and Customer Notification

When imaging is complete, 3NB should:

1. Reconcile chassis and drive/media serials.
2. Verify no extra classified media, labels, notes, or removable devices remain with the asset.
3. Close out lab work notes without adding unnecessary classified details.
4. Notify the customer unit’s CMCC, Security Manager, vault custodian, or COMSEC Manager—not merely the end user.
5. Require the customer to send an appointed courier with courier authorization.

**Security consequence:** notifying only the end user can result in release to a person who lacks authority to accept custody.

---

# 26. Scenario: Return to Customer Unit

Return should mirror intake:

1. Customer courier arrives with valid authorization.
2. 3NB validates courier identity and authority.
3. 3NB and courier physically sight the asset.
4. Both parties validate chassis and drive/media serials.
5. 3NB signs release and closes temporary custody log.
6. Customer signs acceptance and updates its inventory back to “on hand.”
7. Discrepancies are stopped, annotated, reported, and resolved before release when possible.

**Security consequence:** a return without serial reconciliation can transfer an undetected discrepancy back to the customer unit.

---

# 27. Security Violation Severity Guide

| Failure | Likely severity |
|---|---|
| Minor admin error corrected immediately | Infraction |
| Missing signature, incomplete access validation, expired courier card | Infraction to violation |
| Improper storage in unapproved room or unattended case | Violation; possible compromise |
| Release to uncleared/no-need-to-know person | Compromise |
| Asset, hard drive, or COMSEC material cannot be located | Loss |
| Falsified receipt, intentional bypass, or negligent handling | Serious violation; command investigation likely |

DoD characterizes an **infraction** as noncompliance that does not result in loss or compromise; a **violation** may result in loss or compromise; **compromise** means unauthorized disclosure; and **loss** occurs when classified information or equipment cannot be physically located or accounted for.<sup><a href="#ref-27">[27]</a></sup>

---

# 28. Practical Intake Checklist

Before accepting a SIPR asset for imaging, confirm:

- Asset is expected and authorized.
- Courier is appointed and has required documents.
- Packaging is locked, opaque, sealed, and tamper-evident as required.
- Receipt/SF-153 matches physical asset.
- Chassis serial and media serials match.
- Receiving person is appointed and qualified.
- Storage location is approved.
- Temporary custody log is updated immediately.

**Security consequence:** each unchecked item is a potential custody, access, or storage failure.

---

# 29. Practical Return Checklist

Before releasing the asset back to the customer, confirm:

- Imaging is complete.
- Asset and media serials reconcile.
- No extra media or classified notes are included.
- Customer CMCC/security point of contact was notified.
- Courier authority is valid.
- Return receipt is signed by qualified personnel.
- 3NB temporary custody log is closed.
- Customer inventory is updated.

**Security consequence:** a sloppy return can create a false record that hides loss, unauthorized access, or unresolved discrepancy.

---

# 30. Bottom Line

CMCC control is about answering four questions at all times:

1. **What** classified material exists?
2. **Where** is it right now?
3. **Who** is responsible for it?
4. **What record** proves the chain of custody?

For SIPR imaging workflows, the technical task is not complete until the custody record is complete.

**Security consequence:** if the record cannot prove custody, the command may have to treat the situation as a potential loss or compromise.

---

<!-- _class: tiny -->

# References (1/9)

<a id="ref-1"></a>[1]: Department of the Navy, Headquarters Marine Corps, *Marine Corps Order 5510.18B: United States Marine Corps Information and Personnel Security Program*, January 30, 2017, chap. 1, para. 3.c. Official publication page: <https://www.marines.mil/News/Publications/MCPEL/Electronic-Library-Display/Article/1065115/mco-551018b/>. PDF: <https://www.marines.mil/portals/1/Publications/MCO%205510.18B.pdf>.

<a id="ref-2"></a>[2]: Department of the Navy, Headquarters Marine Corps, *MCO 5510.18B*, chap. 4, para. 5.e.(1). Official publication page: <https://www.marines.mil/News/Publications/MCPEL/Electronic-Library-Display/Article/1065115/mco-551018b/>. PDF: <https://www.marines.mil/portals/1/Publications/MCO%205510.18B.pdf>.

<a id="ref-3"></a>[3]: National Institute of Standards and Technology, Computer Security Resource Center, “Communications Security,” glossary entry citing CNSSI 4009-2015 and CNSSI 4005. <https://csrc.nist.gov/glossary/term/communications_security>.

---

<!-- _class: tiny -->

# References (2/9)

<a id="ref-4"></a>[4]: National Institute of Standards and Technology, Computer Security Resource Center, “COMSEC Material,” glossary entry. <https://csrc.nist.gov/glossary/term/comsec_material>.

<a id="ref-5"></a>[5]: National Institute of Standards and Technology, Computer Security Resource Center, “COMSEC Material Control System,” glossary entry. <https://csrc.nist.gov/glossary/term/comsec_material_control_system>.

<a id="ref-6"></a>[6]: National Institute of Standards and Technology, Computer Security Resource Center, “Key Management Infrastructure,” glossary entry citing CNSSI 4009-2015 and CNSSI 4005. <https://csrc.nist.gov/glossary/term/key_management_infrastructure>.

---

<!-- _class: tiny -->

# References (3/9)

<a id="ref-7"></a>[7]: National Institute of Standards and Technology, Computer Security Resource Center, “KMI Operating Account,” glossary entry citing CNSSI 4009-2015. <https://csrc.nist.gov/glossary/term/kmi_operating_account>.

<a id="ref-8"></a>[8]: National Institute of Standards and Technology, Computer Security Resource Center, “Controlled Cryptographic Item,” glossary entry citing CNSSI 4009-2015 and NSA/CSS Manual No. 3-16. <https://csrc.nist.gov/glossary/term/controlled_cryptographic_item>.

<a id="ref-9"></a>[9]: General Services Administration, “COMSEC Material Report,” SF-153 form information, current revision September 1988, last updated February 23, 2026. <https://www.gsa.gov/reference/forms/comsec-material-report>.

---

<!-- _class: tiny -->

# References (4/9)

<a id="ref-10"></a>[10]: Washington Headquarters Services, Executive Services Directorate, “SD 572: Cryptographic Access Certification and Termination,” edition date June 1, 2000. <https://www.esd.whs.mil/Directives/forms/sd_forms/SD572/>.

<a id="ref-11"></a>[11]: Department of Defense, *DoD Manual 5200.01, Volume 3: DoD Information Security Program: Protection of Classified Information*, February 24, 2012, incorporating Change 3, July 28, 2020, encl. 2, sec. 1. <https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520001m_vol3.pdf>.

<a id="ref-12"></a>[12]: Department of Defense, *DoDM 5200.01, Volume 3*, encl. 2, sec. 3. <https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520001m_vol3.pdf>.

---

<!-- _class: tiny -->

# References (5/9)

<a id="ref-13"></a>[13]: Department of Defense, *DoDM 5200.01, Volume 3*, encl. 2, sec. 3, <https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520001m_vol3.pdf>; 32 C.F.R. § 117.21(f), <https://www.ecfr.gov/current/title-32/subtitle-A/chapter-I/subchapter-D/part-117/section-117.21>.

<a id="ref-14"></a>[14]: 32 C.F.R. § 117.21(f)(2)–(4), <https://www.ecfr.gov/current/title-32/subtitle-A/chapter-I/subchapter-D/part-117/section-117.21>; Washington Headquarters Services, “SD 572,” <https://www.esd.whs.mil/Directives/forms/sd_forms/SD572/>.

<a id="ref-15"></a>[15]: Department of the Navy, Headquarters Marine Corps, *MCO 5510.18B*, chap. 4, para. 5.b. Official publication page: <https://www.marines.mil/News/Publications/MCPEL/Electronic-Library-Display/Article/1065115/mco-551018b/>. PDF: <https://www.marines.mil/portals/1/Publications/MCO%205510.18B.pdf>.

---

<!-- _class: tiny -->

# References (6/9)

<a id="ref-16"></a>[16]: Department of the Navy, Headquarters Marine Corps, *MCO 5510.18B*, chap. 4, para. 3. Official publication page: <https://www.marines.mil/News/Publications/MCPEL/Electronic-Library-Display/Article/1065115/mco-551018b/>. PDF: <https://www.marines.mil/portals/1/Publications/MCO%205510.18B.pdf>.

<a id="ref-17"></a>[17]: Department of Defense, *DoDM 5200.01, Volume 3*, encl. 4, sec. 13. <https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520001m_vol3.pdf>.

<a id="ref-18"></a>[18]: Department of Defense, *DoDM 5200.01, Volume 3*, encl. 4, sec. 10. <https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520001m_vol3.pdf>.

---

<!-- _class: tiny -->

# References (7/9)

<a id="ref-19"></a>[19]: Department of Defense, *DoDM 5200.01, Volume 3*, encl. 4, secs. 10–11. <https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520001m_vol3.pdf>.

<a id="ref-20"></a>[20]: Department of Defense, *DoDM 5200.01, Volume 3*, encl. 4, sec. 10.a.(3). <https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520001m_vol3.pdf>.

<a id="ref-21"></a>[21]: Department of Defense, *DoDM 5200.01, Volume 3*, encl. 4, sec. 12.c. <https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520001m_vol3.pdf>.

---

<!-- _class: tiny -->

# References (8/9)

<a id="ref-22"></a>[22]: Department of the Navy, Headquarters Marine Corps, *MCO 5510.18B*, chap. 4, para. 5.b–e. Official publication page: <https://www.marines.mil/News/Publications/MCPEL/Electronic-Library-Display/Article/1065115/mco-551018b/>. PDF: <https://www.marines.mil/portals/1/Publications/MCO%205510.18B.pdf>.

<a id="ref-23"></a>[23]: Department of the Navy, Headquarters Marine Corps, *MCO 5510.18B*, chap. 4, para. 4.b.(3). Official publication page: <https://www.marines.mil/News/Publications/MCPEL/Electronic-Library-Display/Article/1065115/mco-551018b/>. PDF: <https://www.marines.mil/portals/1/Publications/MCO%205510.18B.pdf>.

<a id="ref-24"></a>[24]: Department of the Navy, Headquarters Marine Corps, *MCO 5510.18B*, chap. 4, para. 5.b–d. Official publication page: <https://www.marines.mil/News/Publications/MCPEL/Electronic-Library-Display/Article/1065115/mco-551018b/>. PDF: <https://www.marines.mil/portals/1/Publications/MCO%205510.18B.pdf>.

---

<!-- _class: tiny -->

# References (9/9)

<a id="ref-25"></a>[25]: Department of Defense, *DoDM 5200.01, Volume 3*, encl. 3, sec. 3. <https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520001m_vol3.pdf>.

<a id="ref-26"></a>[26]: Department of Defense, *DoDM 5200.01, Volume 3*, encl. 3, sec. 12.c. <https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520001m_vol3.pdf>.

<a id="ref-27"></a>[27]: Department of Defense, *DoDM 5200.01, Volume 3*, encl. 6, sec. 2.a. <https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520001m_vol3.pdf>.
