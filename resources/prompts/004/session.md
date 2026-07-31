# Tablas y módulo de documentos adjuntos

**Session ID:** ses_080090a76ffeFZAbSQjV6Qh8RQ **Created:** 7/20/2026, 4:38:38 PM
**Updated:** 7/20/2026, 4:47:43 PM

---

## User

He podido ver que a los módulos de Flota, presupuestos, pedidos, etc se le pueden añadir
documentos. Pero me gustaría saber cuales son las tablas que están ligadas, donde se
guardan, estos documentos. Y si hay algún módulo para poder ver todos estos documentos
guardados, sean del modelo que sean. No modifiques nada, sólo contéstame a lo que te
pido.

---

## Assistant (Odoo-Dev · GLM-5.2 · 14.2s)

_Thinking:_

The user is asking a research question about Odoo:

1. What tables are linked to documents that can be added to Fleet modules, quotes,
   orders, etc.
2. Where these documents are stored
3. If there's a module to view all these saved documents regardless of the model

They explicitly said: "No modifiques nada, sólo contéstame a lo que te pido." (Don't
modify anything, just answer what I ask.)

So I should NOT make any edits. I just need to research and answer.

Let me load the skill as required by my instructions for any Odoo development task...
but actually, this is a research question, not a development task. Still, to be safe and
follow instructions, I should investigate the codebase.

Let me think about this:

- In Odoo, attachments/documents are typically stored in `ir.attachment` model (table
  `ir_attachment`).
- The `mail.thread` mixin adds the "log notes" and attachments to models.
- For Fleet: `fleet.vehicle` has a `mail.thread` mixin.
- For Sales orders: `sale.order` has `mail.thread`.
- For Purchase orders: `purchase.order` has `mail.thread`.

The documents attached to records are stored in `ir.attachment` which has:

- `res_model` - the model the attachment is linked to
- `res_id` - the ID of the record
- `name` - filename
- `datas` - the file content (base64 encoded)
- `db_datas` - alternative storage
- `store_fname` - if stored on filesystem
- `type` - 'binary' or 'url'

There's also the Documents app (`documents` module) in Odoo Enterprise that provides a
unified view of all documents.

Let me explore the codebase to confirm and provide specific details.

Since the user asked me not to modify anything, I'll just research. Let me explore the
relevant Odoo core code.

Actually, I should be careful here. The user is asking a conceptual/informational
question. I should answer it thoroughly based on what I find in the codebase. Let me
look at:

1. `ir.attachment` model definition
2. The `mail.thread` mixin
3. The Documents module if available
4. Fleet, Sale, Purchase models to see how they use attachments

Let me start exploring. I don't think I need to load the skill since I'm not editing
anything, but let me re-read the instructions...

The instructions say: "al recibir cualquier tarea de desarrollo Odoo (crear modelos,
vistas, seguridad, wizards, reports, controladores, migraciones, etc.)". This is a
research/informational question, not a development task. And the user explicitly said
don't modify anything.

However, the ABSOLUTE RULE says: "Antes de CUALQUIER edit o write a ficheros bajo
odoo/custom/src/\*\*, DEBES: 1. Llamar al skill tool..." - This is only before any edit
or write. Since I won't be editing, I don't strictly need to load the skill.

But to be thorough and provide a good answer, let me explore the codebase. Let me look
at the relevant models.

Let me start by exploring the structure.

Voy a investigar tu pregunta sin modificar nada. Exploraré el código de Odoo para darte
una respuesta precisa sobre dónde se guardan los documentos de Flota, pedidos,
presupuestos, etc., y si hay un módulo para verlos todos.

**Tool: bash**

**Input:**

```json
{
  "command": "ls /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/",
  "description": "List source addons directories"
}
```

**Output:**

```
addons.yaml
oca
odoo
private
repos.yaml

```

**Tool: glob**

**Input:**

```json
{
  "pattern": "odoo/custom/src/odoo/addons/documents/**/__manifest__.py"
}
```

**Output:**

```
No files found
```

**Tool: glob**

**Input:**

```json
{
  "pattern": "odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment*.py"
}
```

**Output:**

```
No files found
```

---

## Assistant (Odoo-Dev · GLM-5.2 · 3.7s)

_Thinking:_

Let me look for the correct paths.

**Tool: bash**

**Input:**

```json
{
  "command": "ls /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/",
  "description": "List odoo core directory"
}
```

**Output:**

```
addons
CONTRIBUTING.md
COPYRIGHT
debian
doc
LICENSE
MANIFEST.in
odoo
odoo-bin
pyproject.toml
README.md
requirements.txt
SECURITY.md
setup
setup.cfg
setup.py

```

**Tool: glob**

**Input:**

```json
{
  "pattern": "odoo/custom/src/odoo/**/ir_attachment*.py"
}
```

**Output:**

```
No files found
```

---

## Assistant (Odoo-Dev · GLM-5.2 · 3.1s)

**Tool: bash**

**Input:**

```json
{
  "command": "find /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo -name \"ir_attachment*\" -type f 2>/dev/null; echo \"---\"; ls /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ | head -50",
  "description": "Find ir_attachment files and list base models"
}
```

**Output:**

```
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/views/ir_attachment_views.xml
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment.py
---
assetsbundle.py
avatar_mixin.py
decimal_precision.py
image_mixin.py
__init__.py
ir_actions.py
ir_actions_report.py
ir_asset.py
ir_attachment.py
ir_autovacuum.py
ir_binary.py
ir_config_parameter.py
ir_cron.py
ir_default.py
ir_demo_failure.py
ir_demo.py
ir_embedded_actions.py
ir_exports.py
ir_fields.py
ir_filters.py
ir_http.py
ir_logging.py
ir_mail_server.py
ir_model.py
ir_module.py
ir_profile.py
ir_qweb_fields.py
ir_qweb.py
ir_rule.py
ir_sequence.py
ir_ui_menu.py
ir_ui_view.py
report_layout.py
report_paperformat.py
res_bank.py
res_company.py
res_config.py
res_country.py
res_currency.py
res_device.py
res_lang.py
res_partner.py
res_users_deletion.py
res_users.py
res_users_settings.py

```

---

## Assistant (Odoo-Dev · GLM-5.2 · 1.2s)

**Tool: read**

**Input:**

```json
{
  "filePath": "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment.py",
  "limit": 120
}
```

**Output:**

```
<path>/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment.py</path>
<type>file</type>
<content>
1: # Part of Odoo. See LICENSE file for full copyright and licensing details.
2:
3: import base64
4: import binascii
5: import contextlib
6: import hashlib
7: import logging
8: import mimetypes
9: import os
10: import re
11: import uuid
12: from collections import defaultdict
13:
14: import psycopg2
15: import werkzeug
16:
17: from odoo import SUPERUSER_ID, _, api, fields, models, tools
18: from odoo.exceptions import AccessError, UserError, ValidationError
19: from odoo.http import Stream, request, root
20: from odoo.osv import expression
21: from odoo.tools import config, consteq, human_size, image, str2bool
22: from odoo.tools.mimetypes import (
23:     MIMETYPE_HEAD_SIZE,
24:     _olecf_mimetypes,
25:     fix_filename_extension,
26:     guess_mimetype,
27: )
28:
29: _logger = logging.getLogger(__name__)
30:
31:
32: class IrAttachment(models.Model):
33:     """Attachments are used to link binary files or url to any openerp document.
34:
35:     External attachment storage
36:     ---------------------------
37:
38:     The computed field ``datas`` is implemented using ``_file_read``,
39:     ``_file_write`` and ``_file_delete``, which can be overridden to implement
40:     other storage engines. Such methods should check for other location pseudo
41:     uri (example: hdfs://hadoopserver).
42:
43:     The default implementation is the file:dirname location that stores files
44:     on the local filesystem using name based on their sha1 hash
45:     """
46:     _name = 'ir.attachment'
47:     _description = 'Attachment'
48:     _order = 'id desc'
49:
50:     def _compute_res_name(self):
51:         for attachment in self:
52:             if attachment.res_model and attachment.res_id:
53:                 record = self.env[attachment.res_model].browse(attachment.res_id)
54:                 attachment.res_name = record.display_name
55:             else:
56:                 attachment.res_name = False
57:
58:     @api.model
59:     def _storage(self):
60:         return self.env['ir.config_parameter'].sudo().get_param('ir_attachment.location', 'file')
61:
62:     @api.model
63:     def _filestore(self):
64:         return config.filestore(self._cr.dbname)
65:
66:     @api.model
67:     def _get_storage_domain(self):
68:         # domain to retrieve the attachments to migrate
69:         return {
70:             'db': [('store_fname', '!=', False)],
71:             'file': [('db_datas', '!=', False)],
72:         }[self._storage()]
73:
74:     @api.model
75:     def force_storage(self):
76:         """Force all attachments to be stored in the currently configured storage"""
77:         if not self.env.is_admin():
78:             raise AccessError(_('Only administrators can execute this action.'))
79:
80:         # Migrate only binary attachments and bypass the res_field automatic
81:         # filter added in _search override
82:         self.search(expression.AND([
83:             self._get_storage_domain(),
84:             ['&', ('type', '=', 'binary'), '|', ('res_field', '=', False), ('res_field', '!=', False)]
85:         ]))._migrate()
86:
87:     def _migrate(self):
88:         record_count = len(self)
89:         storage = self._storage().upper()
90:         # When migrating to filestore verifying if the directory has write permission
91:         if storage == 'FILE':
92:             filestore = self._filestore()
93:             if not os.access(filestore, os.W_OK):
94:                 raise PermissionError("Write permission denied for filestore directory.")
95:         for index, attach in enumerate(self):
96:             _logger.debug("Migrate attachment %s/%s to %s", index + 1, record_count, storage)
97:             # pass mimetype, to avoid recomputation
98:             attach.write({'raw': attach.raw, 'mimetype': attach.mimetype})
99:
100:     @api.model
101:     def _full_path(self, path):
102:         # sanitize path
103:         path = re.sub('[.]', '', path)
104:         path = path.strip('/\\')
105:         return os.path.join(self._filestore(), path)
106:
107:     @api.model
108:     def _get_path(self, bin_data, sha):
109:         # scatter files across 256 dirs
110:         # we use '/' in the db (even on windows)
111:         fname = sha[:2] + '/' + sha
112:         full_path = self._full_path(fname)
113:         dirname = os.path.dirname(full_path)
114:         if not os.path.isdir(dirname):
115:             os.makedirs(dirname, exist_ok=True)
116:
117:         # prevent sha-1 collision
118:         if os.path.isfile(full_path) and not self._same_content(bin_data, full_path):
119:             raise UserError(_("The attachment collides with an existing file."))
120:         return fname, full_path

(Showing lines 1-120 of 861. Use offset=121 to continue.)
</content>
```

---

## Assistant (Odoo-Dev · GLM-5.2 · 2.4s)

_Thinking:_

Let me look at the field definitions of ir.attachment to understand the structure.

**Tool: read**

**Input:**

```json
{
  "filePath": "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment.py",
  "offset": 200,
  "limit": 200
}
```

**Output:**

```
<path>/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment.py</path>
<type>file</type>
<content>
200:         for dirpath, _, filenames in os.walk(self._full_path('checklist')):
201:             dirname = os.path.basename(dirpath)
202:             for filename in filenames:
203:                 fname = "%s/%s" % (dirname, filename)
204:                 checklist[fname] = os.path.join(dirpath, filename)
205:
206:         # Clean up the checklist. The checklist is split in chunks and files are garbage-collected
207:         # for each chunk.
208:         removed = 0
209:         for names in self.env.cr.split_for_in_conditions(checklist):
210:             # determine which files to keep among the checklist
211:             self.env.cr.execute("SELECT store_fname FROM ir_attachment WHERE store_fname IN %s", [names])
212:             whitelist = set(row[0] for row in self.env.cr.fetchall())
213:
214:             # remove garbage files, and clean up checklist
215:             for fname in names:
216:                 filepath = checklist[fname]
217:                 if fname not in whitelist:
218:                     try:
219:                         os.unlink(self._full_path(fname))
220:                         _logger.debug("_file_gc unlinked %s", self._full_path(fname))
221:                         removed += 1
222:                     except (OSError, IOError):
223:                         _logger.info("_file_gc could not unlink %s", self._full_path(fname), exc_info=True)
224:                 with contextlib.suppress(OSError):
225:                     os.unlink(filepath)
226:
227:         _logger.info("filestore gc %d checked, %d removed", len(checklist), removed)
228:
229:     @api.depends('store_fname', 'db_datas', 'file_size')
230:     @api.depends_context('bin_size')
231:     def _compute_datas(self):
232:         if self._context.get('bin_size'):
233:             for attach in self:
234:                 attach.datas = human_size(attach.file_size)
235:             return
236:
237:         for attach in self:
238:             attach.datas = base64.b64encode(attach.raw or b'')
239:
240:     @api.depends('store_fname', 'db_datas')
241:     def _compute_raw(self):
242:         for attach in self:
243:             if attach.store_fname:
244:                 attach.raw = attach._file_read(attach.store_fname)
245:             else:
246:                 attach.raw = attach.db_datas
247:
248:     def _inverse_raw(self):
249:         self._set_attachment_data(lambda a: a.raw or b'')
250:
251:     def _inverse_datas(self):
252:         self._set_attachment_data(lambda attach: base64.b64decode(attach.datas or b''))
253:
254:     def _set_attachment_data(self, asbytes):
255:         for attach in self:
256:             # compute the fields that depend on datas
257:             bin_data = asbytes(attach)
258:             vals = self._get_datas_related_values(bin_data, attach.mimetype)
259:
260:             # take current location in filestore to possibly garbage-collect it
261:             fname = attach.store_fname
262:             # write as superuser, as user probably does not have write access
263:             super(IrAttachment, attach.sudo()).write(vals)
264:             if fname:
265:                 self._file_delete(fname)
266:
267:     def _get_datas_related_values(self, data, mimetype):
268:         checksum = self._compute_checksum(data)
269:         try:
270:             index_content = self._index(data, mimetype, checksum=checksum)
271:         except TypeError:
272:             index_content = self._index(data, mimetype)
273:         values = {
274:             'file_size': len(data),
275:             'checksum': checksum,
276:             'index_content': index_content,
277:             'store_fname': False,
278:             'db_datas': data,
279:         }
280:         if data and self._storage() != 'db':
281:             values['store_fname'] = self._file_write(data, values['checksum'])
282:             values['db_datas'] = False
283:         return values
284:
285:     def _compute_checksum(self, bin_data):
286:         """ compute the checksum for the given datas
287:             :param bin_data : datas in its binary form
288:         """
289:         # an empty file has a checksum too (for caching)
290:         return hashlib.sha1(bin_data or b'').hexdigest()
291:
292:     @api.model
293:     def _same_content(self, bin_data, filepath):
294:         BLOCK_SIZE = 1024
295:         with open(filepath, 'rb') as fd:
296:             i = 0
297:             while True:
298:                 data = fd.read(BLOCK_SIZE)
299:                 if data != bin_data[i * BLOCK_SIZE:(i + 1) * BLOCK_SIZE]:
300:                     return False
301:                 if not data:
302:                     break
303:                 i += 1
304:         return True
305:
306:     def _compute_mimetype(self, values):
307:         """ compute the mimetype of the given values
308:             :param values : dict of values to create or write an ir_attachment
309:             :return mime : string indicating the mimetype, or application/octet-stream by default
310:         """
311:         mimetype = None
312:         if values.get('mimetype'):
313:             mimetype = values['mimetype']
314:         if not mimetype and values.get('name'):
315:             mimetype = mimetypes.guess_type(values['name'])[0]
316:         if not mimetype and values.get('url'):
317:             mimetype = mimetypes.guess_type(values['url'].split('?')[0])[0]
318:         if not mimetype or mimetype == 'application/octet-stream':
319:             raw = None
320:             if values.get('raw'):
321:                 raw = values['raw']
322:             elif values.get('datas'):
323:                 raw = base64.b64decode(values['datas'])
324:             if raw:
325:                 mimetype = guess_mimetype(raw)
326:         return mimetype and mimetype.lower() or 'application/octet-stream'
327:
328:     def _postprocess_contents(self, values):
329:         ICP = self.env['ir.config_parameter'].sudo().get_param
330:         supported_subtype = ICP('base.image_autoresize_extensions', 'png,jpeg,bmp,tiff').split(',')
331:
332:         mimetype = values['mimetype'] = self._compute_mimetype(values)
333:         _type, _match, _subtype = mimetype.partition('/')
334:         is_image_resizable = _type == 'image' and _subtype in supported_subtype
335:         if is_image_resizable and (values.get('datas') or values.get('raw')):
336:             is_raw = values.get('raw')
337:
338:             # Can be set to 0 to skip the resize
339:             max_resolution = ICP('base.image_autoresize_max_px', '1920x1920')
340:             if str2bool(max_resolution, True):
341:                 try:
342:                     if is_raw:
343:                         img = image.ImageProcess(values['raw'], verify_resolution=False)
344:                     else:  # datas
345:                         img = image.ImageProcess(base64.b64decode(values['datas']), verify_resolution=False)
346:
347:                     if not img.image:
348:                         _logger.info('Post processing ignored : Empty source, SVG, or WEBP')
349:                         return values
350:
351:                     w, h = img.image.size
352:                     nw, nh = map(int, max_resolution.split('x'))
353:                     if w > nw or h > nh:
354:                         img = img.resize(nw, nh)
355:                         if _subtype == 'jpeg':  # Do not affect PNGs color palette
356:                             quality = int(ICP('base.image_autoresize_quality', 80))
357:                         else:
358:                             quality = 0
359:                         image_data = img.image_quality(quality=quality)
360:                         if is_raw:
361:                             values['raw'] = image_data
362:                         else:
363:                             values['datas'] = base64.b64encode(image_data)
364:                 except UserError as e:
365:                     # Catch error during test where we provide fake image
366:                     # raise UserError(_("This file could not be decoded as an image file. Please try with a different file."))
367:                     msg = str(e)  # the exception can be lazy-translated, resolve it here
368:                     _logger.info('Post processing ignored : %s', msg)
369:         return values
370:
371:     def _check_contents(self, values):
372:         mimetype = values['mimetype'] = self._compute_mimetype(values)
373:         xml_like = 'ht' in mimetype or ( # hta, html, xhtml, etc.
374:                 'xml' in mimetype and    # other xml (svg, text/xml, etc)
375:                 not mimetype.startswith('application/vnd.openxmlformats'))  # exception for Office formats
376:         force_text = xml_like and (
377:             self.env.context.get('attachments_mime_plainxml')
378:             or not self.env['ir.ui.view'].sudo(False).has_access('write')
379:         )
380:         if force_text:
381:             values['mimetype'] = 'text/plain'
382:         if not self.env.context.get('image_no_postprocess'):
383:             values = self._postprocess_contents(values)
384:         return values
385:
386:     @api.model
387:     def _index(self, bin_data, file_type, checksum=None):
388:         """ compute the index content of the given binary data.
389:             This is a python implementation of the unix command 'strings'.
390:             :param bin_data : datas in binary form
391:             :return index_content : string containing all the printable character of the binary data
392:         """
393:         index_content = False
394:         if file_type:
395:             index_content = file_type.split('/')[0]
396:             if index_content == 'text': # compute index_content only for text type
397:                 words = re.findall(b"[\x20-\x7E]{4,}", bin_data)
398:                 index_content = b"\n".join(words).decode('ascii')
399:         return index_content

(Showing lines 200-399 of 861. Use offset=400 to continue.)
</content>
```

---

## Assistant (Odoo-Dev · GLM-5.2 · 5.0s)

_Thinking:_

Let me find the field definitions for ir.attachment.

**Tool: grep**

**Input:**

```json
{
  "pattern": "_name = ['\\\"]ir.attachment['\\\"]|_description|res_model|res_id|store_fname|db_datas|name = fields|^    name |res_name|type = fields|mimetype|public|url = fields|checksum",
  "path": "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment.py"
}
```

**Output:**

```
Found 100 matches (more matches available)
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/report_paperformat.py:
  Line 168:     _description = "Paper Format Config"

  Line 170:     name = fields.Char('Name', required=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_logging.py:
  Line 7:     _description = 'Logging'

  Line 27:     name = fields.Char(required=True)

  Line 28:     type = fields.Selection([('client', 'Client'), ('server', 'Server')], required=True, index=True)

  Line 29:     dbname = fields.Char(string='Database Name', index=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_embedded_actions.py:
  Line 10:     _description = 'Embedded Actions'

  Line 13:     name = fields.Char(translate=True)

  Line 16:     parent_res_id = fields.Integer(string="Active Parent Id")

  Line 17:     parent_res_model = fields.Char(string='Active Parent Model', required=True)

  Line 40:             'check_python_method_requires_name',

  Line 88:         for parent_res_model, records in self.grouped('parent_res_model').items():

  Line 89:             active_model_record = self.env[parent_res_model].search(domain_id, order='id')

  Line 95:                         record.parent_res_id in (False, self.env.context.get('active_id', False))

  Line 113:             "name", "parent_action_id", "parent_res_id", "parent_res_model", "action_id", "python_method", "user_id",


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_country.py:
  Line 34:     _description = 'Country'

  Line 38:     name = fields.Char(

  Line 61:     image_url = fields.Char(

  Line 154:     _description = "Country Group"

  Line 157:     name = fields.Char(required=True, translate=True)

  Line 163:     _description = "Country state"

  Line 169:     name = fields.Char(string='State Name', required=True,


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/image_mixin.py:
  Line 9:     _description = "Image Mixin"


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_device.py:
  Line 18:     _description = 'Device Log'

  Line 27:     device_type = fields.Selection([('computer', 'Computer'), ('mobile', 'Mobile')], "Device Type")

  Line 178:     _description = "Devices"


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_users_settings.py:
  Line 9:     _description = 'User Settings'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_rule.py:
  Line 14:     _description = 'Record Rule'

  Line 19:     name = fields.Char(index=True)

  Line 217:         user_description = f"{self.env.user.name} (id={self.env.user.id})"

  Line 219:             "Sorry, %(user)s doesn't have '%(operation)s' access to:", user=user_description, operation=operations[operation])

  Line 224:         # Note that by default, public and portal users do not have

  Line 232:         def get_record_description(rec):

  Line 254:             failing_records = '\n'.join(f'- {get_record_description(rec)}' for rec in records_sudo)

  Line 255:             rules_description = '\n'.join(f'- {rule.name}' for rule in rules)

  Line 256:             failing_rules = _("Blame the following rules:\n%s", rules_description)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_users_deletion.py:
  Line 24:     _description = 'Users Deletion Request'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_lang.py:
  Line 53:     _description = "Languages"

  Line 60:     name = fields.Char(required=True)

  Line 93:     flag_image_url = fields.Char(compute=_compute_field_flag_image_url)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_filters.py:
  Line 11:     _description = 'Filters'

  Line 14:     name = fields.Char(string='Filter Name', required=True)

  Line 16:                               help="The user this filter is private to. When left empty the filter is public "

  Line 28:     embedded_parent_res_id = fields.Integer(help="id of the record the filter should be applied to. Only used in combination with embedded actions")

  Line 43:         # check_res_id_only_when_embedded_action

  Line 45:             if vals.get('embedded_parent_res_id') == 0:

  Line 46:                 del vals['embedded_parent_res_id']

  Line 62:     def _get_action_domain(self, action_id=None, embedded_action_id=None, embedded_parent_res_id=None):

  Line 67:         embedded_parent_res_id_condition = ('embedded_parent_res_id', '=', embedded_parent_res_id) if embedded_action_id and embedded_parent_res_id else ('embedded_parent_res_id', 'in', [0, False])

  Line 69:         return [action_condition, embedded_condition, embedded_parent_res_id_condition]

  Line 72:     def get_filters(self, model, action_id=None, embedded_action_id=None, embedded_parent_res_id=None):

  Line 82:             ``action_id`` (m2o tuple), ``embedded_action_id`` (m2o tuple), ``embedded_parent_res_id``

  Line 85:         # available filters: private filters (user_id=uid) and public filters (uid=NULL),

  Line 88:         action_domain = self._get_action_domain(action_id, embedded_action_id, embedded_parent_res_id)

  Line 91:             ['name', 'is_default', 'domain', 'context', 'user_id', 'sort', 'embedded_action_id', 'embedded_parent_res_id'],

  Line 111:         domain = self._get_action_domain(vals.get('action_id'), vals.get('embedded_action_id'), vals.get('embedded_parent_res_id'))

  Line 130:         if not embedded_action_id and 'embedded_parent_res_id' in vals:

  Line 131:             del vals['embedded_parent_res_id']

  Line 132:         embedded_parent_res_id = vals.get('embedded_parent_res_id')

  Line 133:         current_filters = self.get_filters(vals['model_id'], action_id, embedded_action_id, embedded_parent_res_id)

  Line 145:                 domain = self._get_action_domain(action_id, embedded_action_id, embedded_parent_res_id)

  Line 169:         ('name_model_uid_unique', 'unique (model_id, user_id, action_id, embedded_action_id, embedded_parent_res_id, name)',

  Line 172:         # The embedded_parent_res_id can only be defined when the embedded_action_id field is set.

  Line 173:         # As the embedded model is linked to only one res_model, It ensure the unicity of the filter regarding the

  Line 174:         # embedded_parent_res_model and the embedded_parent_res_id

  Line 176:             'check_res_id_only_when_embedded_action',

  Line 178:                 NOT (embedded_parent_res_id IS NOT NULL AND embedded_action_id IS NULL)

  Line 180:             'Constraint to ensure that the embedded_parent_res_id is only defined when a top_action_id is defined.'

  Line 190:                                                 'lower(name)', 'embedded_parent_res_id', 'COALESCE(embedded_action_id,-1)'])


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_asset.py:
  Line 62:     _description = 'Asset'

  Line 80:     name = fields.Char(string='Name', required=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_bank.py:
  Line 17:     _description = 'Bank'

  Line 22:     name = fields.Char(required=True)

  Line 64:     _description = 'Bank Accounts'

  Line 77:     acc_type = fields.Selection(selection=lambda x: x.env['res.partner.bank'].get_supported_account_types(), compute='_compute_acc_type', string='Type', help='Bank account type: Normal or IBAN. Inferred from the bank account number.')

  Line 80:     acc_holder_name = fields.Char(string='Account Holder Name', help="Account holder name, in case it is different than the name of the Account Holder", compute='_compute_account_holder_name', readonly=False, store=True)

  Line 84:     bank_name = fields.Char(related='bank_id.name', readonly=False)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_demo.py:
  Line 12:     _description = 'Demo'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/avatar_mixin.py:
  Line 24:     _description = "Avatar Mixin"


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_company.py:
  Line 19:     _description = 'Companies'

  Line 34:     name = fields.Char(related='partner_id.name', string='Company Name', required=True, store=True, readonly=False)

  Line 428:                         description = self.env['ir.model.fields']._get("res.company", fname).field_description

  Line 477:             'res_model': 'res.company',

  Line 486:     def _get_public_user(self):

  Line 488:         # We need sudo to be able to see public users from others companies too

  Line 489:         public_users = self.env.ref('base.group_public').sudo().with_context(active_test=False).users

  Line 490:         public_users_for_company = public_users.filtered(lambda user: user.company_id == self)

  Line 492:         if public_users_for_company:

  Line 493:             return public_users_for_company[0]

  Line 495:             return self.env.ref('base.public_user').sudo().copy({

  Line 497:                 'login': 'public-user@company-%s.com' % self.id,


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/decimal_precision.py:
  Line 19:     _description = 'Decimal Precision'

  Line 21:     name = fields.Char('Usage', required=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/assetsbundle.py:
  Line 73:         self._checksum_cache = {}

  Line 128:         return self.get_checksum(asset_type)[0:7]

  Line 130:     def get_checksum(self, asset_type):

  Line 132:         Not really a full checksum.

  Line 135:         if asset_type not in self._checksum_cache:

  Line 145:             self._checksum_cache[asset_type] = hashlib.sha512(unique_descriptor.encode()).hexdigest()[:64]

  Line 146:         return self._checksum_cache[asset_type]


(Results truncated. Consider using a more specific path or pattern.)
```

---

## Assistant (Odoo-Dev · GLM-5.2 · 2.6s)

_Thinking:_

Let me read the field definitions directly in ir_attachment.py.

**Tool: grep**

**Input:**

```json
{
  "path": "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment.py",
  "pattern": "^\\s+(name|res_model|res_id|res_name|store_fname|db_datas|type|mimetype|public|url|checksum|file_size|index_content|raw|datas|create_date|create_uid|write_date|write_uid|description|company_id)\\s*=\\s*fields"
}
```

**Output:**

```
Found 97 matches
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_default.py:
  Line 23:     company_id = fields.Many2one('res.company', string='Company', ondelete='cascade', index=True,


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_exports.py:
  Line 12:     name = fields.Char(string='Export Name')

  Line 22:     name = fields.Char(string='Field Name')


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_ui_view.py:
  Line 149:     name = fields.Char(string='View Name', required=True)

  Line 153:     type = fields.Selection([('list', 'List'),


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_rule.py:
  Line 19:     name = fields.Char(index=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_embedded_actions.py:
  Line 13:     name = fields.Char(translate=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_country.py:
  Line 38:     name = fields.Char(

  Line 157:     name = fields.Char(required=True, translate=True)

  Line 169:     name = fields.Char(string='State Name', required=True,


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_bank.py:
  Line 22:     name = fields.Char(required=True)

  Line 88:     company_id = fields.Many2one('res.company', 'Company', related='partner_id.company_id', store=True, readonly=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_partner.py:
  Line 151:     name = fields.Char('Name', required=True, translate=True)

  Line 189:     name = fields.Char(string='Title', required=True, translate=True)

  Line 225:     name = fields.Char(index=True, default_export_compatible=True)

  Line 263:     type = fields.Selection(

  Line 1126:     name = fields.Char('Name', translate=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_sequence.py:
  Line 126:     name = fields.Char(required=True)

  Line 146:     company_id = fields.Many2one('res.company', string='Company',


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_profile.py:
  Line 27:     create_date = fields.Datetime('Creation Date')

  Line 30:     name = fields.Char('Description')


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_company.py:
  Line 34:     name = fields.Char(related='partner_id.name', string='Company Name', required=True, store=True, readonly=False)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/decimal_precision.py:
  Line 21:     name = fields.Char('Usage', required=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_actions_report.py:
  Line 146:     type = fields.Char(default='ir.actions.report')


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_ui_menu.py:
  Line 26:     name = fields.Char(string='Menu', required=True, translate=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/report_layout.py:
  Line 17:     name = fields.Char()


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_module.py:
  Line 86:     name = fields.Char(string='Name', required=True, translate=True, index=True)

  Line 90:     description = fields.Text(string='Description', translate=True)

  Line 288:     name = fields.Char('Technical Name', readonly=True, required=True)

  Line 292:     description = fields.Text('Description', readonly=True, translate=True)

  Line 307:     url = fields.Char('URL', readonly=True)

  Line 1002:     name = fields.Char(index=True)

  Line 1066:     name = fields.Char(index=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_actions.py:
  Line 61:     name = fields.Char(string='Action Name', required=True, translate=True)

  Line 62:     type = fields.Char(string='Action Type', required=True)

  Line 302:     type = fields.Char(default="ir.actions.act_window")

  Line 308:     res_id = fields.Integer(string='Record ID', help="Database ID of record to open in form view, when ``view_mode`` is set to 'form' only")

  Line 309:     res_model = fields.Char(string='Destination Model', required=True,

  Line 436:     type = fields.Char(default='ir.actions.act_window_close')

  Line 454:     type = fields.Char(default='ir.actions.act_url')

  Line 455:     url = fields.Text(string='Action URL', required=True)

  Line 536:     name = fields.Char(required=True)

  Line 537:     type = fields.Char(default='ir.actions.server')

  Line 1102:     name = fields.Char()

  Line 1176:     type = fields.Char(default='ir.actions.client')

  Line 1183:     res_model = fields.Char(string='Destination Model', help="Optional model, mostly used for needactions.")


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_filters.py:
  Line 14:     name = fields.Char(string='Filter Name', required=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment.py:
  Line 410:     name = fields.Char('Name', required=True)

  Line 411:     description = fields.Text('Description')

  Line 412:     res_name = fields.Char('Resource Name', compute='_compute_res_name')

  Line 413:     res_model = fields.Char('Resource Model')

  Line 415:     res_id = fields.Many2oneReference('Resource ID', model_field='res_model')

  Line 416:     company_id = fields.Many2one('res.company', string='Company', change_default=True,

  Line 418:     type = fields.Selection([('url', 'URL'), ('binary', 'File')],

  Line 421:     url = fields.Char('Url', index='btree_not_null', size=1024)

  Line 422:     public = fields.Boolean('Is public document')

  Line 428:     raw = fields.Binary(string="File Content (raw)", compute='_compute_raw', inverse='_inverse_raw')

  Line 429:     datas = fields.Binary(string='File Content (base64)', compute='_compute_datas', inverse='_inverse_datas')

  Line 430:     db_datas = fields.Binary('Database Data', attachment=False)

  Line 431:     store_fname = fields.Char('Stored Filename', index=True)

  Line 432:     file_size = fields.Integer('File Size', readonly=True)

  Line 433:     checksum = fields.Char("Checksum/SHA1", size=40, readonly=True)

  Line 434:     mimetype = fields.Char('Mime Type', readonly=True)

  Line 435:     index_content = fields.Text('Indexed Content', readonly=True, prefetch=False)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/report_paperformat.py:
  Line 170:     name = fields.Char('Name', required=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_lang.py:
  Line 60:     name = fields.Char(required=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_currency.py:
  Line 29:     name = fields.Char(string='Currency', size=3, required=True, help="Currency Code (ISO 4217)")

  Line 345:     name = fields.Date(string='Date', required=True, index=True,

  Line 368:     company_id = fields.Many2one('res.company', string='Company',


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_model.py:
  Line 225:     name = fields.Char(string='Model Description', translate=True, required=True)

  Line 552:     name = fields.Char(string='Field Name', default='x_', required=True, index=True)

  Line 1527:     name = fields.Char(translate=True, required=True)

  Line 1865:     name = fields.Char(string='Constraint', required=True, index=True,

  Line 1871:     type = fields.Char(string='Constraint Type', required=True, size=1, index=True,

  Line 1874:     write_date = fields.Datetime()

  Line 1875:     create_date = fields.Datetime()

  Line 2019:     name = fields.Char(string='Relation Name', required=True, index=True,

  Line 2023:     write_date = fields.Datetime()

  Line 2024:     create_date = fields.Datetime()

  Line 2082:     name = fields.Char(required=True, index=True)

  Line 2238:     name = fields.Char(string='External Identifier', required=True,

  Line 2244:     res_id = fields.Many2oneReference(string='Record ID', help="ID of the target record in the database", model_field='model')

  Line 2738:     name = fields.Char(string='Menu Name', required=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_mail_server.py:
  Line 154:     name = fields.Char(string='Name', required=True, index=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_logging.py:
  Line 22:     create_uid = fields.Integer(string='Created by', readonly=True)

  Line 23:     create_date = fields.Datetime(string='Created on', readonly=True)

  Line 24:     write_uid = fields.Integer(string='Last Updated by', readonly=True)

  Line 25:     write_date = fields.Datetime(string='Last Updated on', readonly=True)

  Line 27:     name = fields.Char(required=True)

  Line 28:     type = fields.Selection([('client', 'Client'), ('server', 'Server')], required=True, index=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/res_users.py:
  Line 183:     name = fields.Char(required=True, translate=True)

  Line 401:     company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company.id,

  Line 408:     name = fields.Char(related='partner_id.name', inherited=True, readonly=False)

  Line 2355:     name = fields.Char("Description", required=True, readonly=True)

  Line 2358:     create_date = fields.Datetime("Creation Date", readonly=True)

  Line 2495:     name = fields.Char("Description", required=True)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_asset.py:
  Line 80:     name = fields.Char(string='Name', required=True)

```

---

## Assistant (Odoo-Dev · GLM-5.2 · 2.2s)

_Thinking:_

Now I have the field definitions for ir.attachment. Let me look at lines 405-440 of
ir_attachment.py to see the complete field list.

**Tool: read**

**Input:**

```json
{
  "filePath": "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment.py",
  "offset": 400,
  "limit": 45
}
```

**Output:**

```
<path>/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment.py</path>
<type>file</type>
<content>
400:
401:     @api.model
402:     def get_serving_groups(self):
403:         """ An ir.attachment record may be used as a fallback in the
404:         http dispatch if its type field is set to "binary" and its url
405:         field is set as the request's url. Only the groups returned by
406:         this method are allowed to create and write on such records.
407:         """
408:         return ['base.group_system']
409:
410:     name = fields.Char('Name', required=True)
411:     description = fields.Text('Description')
412:     res_name = fields.Char('Resource Name', compute='_compute_res_name')
413:     res_model = fields.Char('Resource Model')
414:     res_field = fields.Char('Resource Field')
415:     res_id = fields.Many2oneReference('Resource ID', model_field='res_model')
416:     company_id = fields.Many2one('res.company', string='Company', change_default=True,
417:                                  default=lambda self: self.env.company)
418:     type = fields.Selection([('url', 'URL'), ('binary', 'File')],
419:                             string='Type', required=True, default='binary', change_default=True,
420:                             help="You can either upload a file from your computer or copy/paste an internet link to your file.")
421:     url = fields.Char('Url', index='btree_not_null', size=1024)
422:     public = fields.Boolean('Is public document')
423:
424:     # for external access
425:     access_token = fields.Char('Access Token', groups="base.group_user")
426:
427:     # the field 'datas' is computed and may use the other fields below
428:     raw = fields.Binary(string="File Content (raw)", compute='_compute_raw', inverse='_inverse_raw')
429:     datas = fields.Binary(string='File Content (base64)', compute='_compute_datas', inverse='_inverse_datas')
430:     db_datas = fields.Binary('Database Data', attachment=False)
431:     store_fname = fields.Char('Stored Filename', index=True)
432:     file_size = fields.Integer('File Size', readonly=True)
433:     checksum = fields.Char("Checksum/SHA1", size=40, readonly=True)
434:     mimetype = fields.Char('Mime Type', readonly=True)
435:     index_content = fields.Text('Indexed Content', readonly=True, prefetch=False)
436:
437:     def _auto_init(self):
438:         res = super(IrAttachment, self)._auto_init()
439:         tools.create_index(self._cr, 'ir_attachment_res_idx',
440:                            self._table, ['res_model', 'res_id'])
441:         return res
442:
443:     @api.constrains('type', 'url')
444:     def _check_serving_attachments(self):

(Showing lines 400-444 of 861. Use offset=445 to continue.)
</content>
```

---

## Assistant (Odoo-Dev · GLM-5.2 · 9.5s)

_Thinking:_

Now I have the complete picture of the `ir.attachment` model fields. Let me now verify
the mail.thread mixin and how Fleet, Sale, Purchase models use it.

Let me also check if there's a `documents` module in OCA or if it's enterprise-only.

Ahora déjame verificar el `mail.thread` mixin y cómo lo usan Flota, Ventas y Compras,
además de comprobar si hay módulo de Documents en OCA.

**Tool: bash**

**Input:**

```json
{
  "command": "ls /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/ 2>/dev/null; echo \"---OCA docs?---\"; find /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca -maxdepth 2 -type d -iname \"*document*\" 2>/dev/null; echo \"---core docs?---\"; find /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons -maxdepth 1 -type d -iname \"*document*\" 2>/dev/null",
  "description": "Check for documents modules in OCA and core"
}
```

**Output:**

```
bank-payment
community-data-files
knowledge
l10n-spain
web
---OCA docs?---
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_page_partner
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_page_access_group_user_role
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_knowledge
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_url
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_page
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_page_project_task
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_page_group
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_page_project
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_page_reference
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_page_approval
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_page_access_group
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_page_product
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_page_tag
---core docs?---
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/l10n_latam_invoice_document

```

**Tool: grep**

**Input:**

```json
{
  "path": "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/fleet_vehicle.py",
  "pattern": "_mail_thread|_name = |_inherit = |class Fleet|mail.thread"
}
```

**Output:**

```
Found 32 matches
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/fleet_vehicle_odometer.py:
  Line 7: class FleetVehicleOdometer(models.Model):

  Line 8:     _name = 'fleet.vehicle.odometer'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/res_config_settings.py:
  Line 8:     _inherit = ['res.config.settings']


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/mail_activity_type.py:
  Line 5:     _inherit = "mail.activity.type"


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/fleet_vehicle_state.py:
  Line 7: class FleetVehicleState(models.Model):

  Line 8:     _name = 'fleet.vehicle.state'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/fleet_vehicle_model_category.py:
  Line 7: class FleetVehicleModelCategory(models.Model):

  Line 8:     _name = 'fleet.vehicle.model.category'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/fleet_vehicle_model_brand.py:
  Line 7: class FleetVehicleModelBrand(models.Model):

  Line 8:     _name = 'fleet.vehicle.model.brand'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/fleet_vehicle_tag.py:
  Line 7: class FleetVehicleTag(models.Model):

  Line 8:     _name = 'fleet.vehicle.tag'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/fleet_vehicle_log_contract.py:
  Line 9: class FleetVehicleLogContract(models.Model):

  Line 10:     _inherit = ['mail.thread', 'mail.activity.mixin']

  Line 11:     _name = 'fleet.vehicle.log.contract'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/fleet_service_type.py:
  Line 7: class FleetServiceType(models.Model):

  Line 8:     _name = 'fleet.service.type'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/fleet_vehicle.py:
  Line 21: class FleetVehicle(models.Model):

  Line 22:     _inherit = ['mail.thread', 'mail.activity.mixin', 'avatar.mixin']

  Line 23:     _name = 'fleet.vehicle'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/fleet_vehicle_model.py:
  Line 20: class FleetVehicleModel(models.Model):

  Line 21:     _name = 'fleet.vehicle.model'

  Line 22:     _inherit = ['mail.thread', 'mail.activity.mixin', 'avatar.mixin']

  Line 71:             record.display_name = name


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/res_partner.py:
  Line 8:     _inherit = 'res.partner'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/fleet_vehicle_assignation_log.py:
  Line 7: class FleetVehicleAssignationLog(models.Model):

  Line 8:     _name = "fleet.vehicle.assignation.log"

  Line 20:             rec.display_name = f'{rec.vehicle_id.name} - {rec.driver_id.name}'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/fleet/models/fleet_vehicle_log_services.py:
  Line 8: class FleetVehicleLogServices(models.Model):

  Line 9:     _name = 'fleet.vehicle.log.services'

  Line 10:     _inherit = ['mail.thread', 'mail.activity.mixin']

  Line 11:     _rec_name = 'service_type_id'

```

**Tool: grep**

**Input:**

```json
{
  "path": "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/sale_order.py",
  "pattern": "class SaleOrder|_name = ['\\\"]sale.order|mail.thread|_inherit"
}
```

**Output:**

```
Found 25 matches
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/product_template.py:
  Line 13:     _inherit = 'product.template'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/product_category.py:
  Line 5:     _inherit = "product.category"


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/sale_order.py:
  Line 49: class SaleOrder(models.Model):

  Line 50:     _name = 'sale.order'

  Line 51:     _inherit = ['portal.mixin', 'product.catalog.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/account_move_line.py:
  Line 9:     _inherit = 'account.move.line'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/res_company.py:
  Line 8:     _inherit = 'res.company'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/chart_template.py:
  Line 5:     _inherit = 'account.chart.template'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/product_product.py:
  Line 11:     _inherit = 'product.product'

  Line 103:     _inherit = "product.attribute.custom.value"

  Line 112:     _inherit = 'product.packaging'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/analytic.py:
  Line 8:     _inherit = "account.analytic.line"

  Line 14:     _inherit = 'account.analytic.applicability'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/utm_campaign.py:
  Line 7:     _inherit = 'utm.campaign'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/product_document.py:
  Line 7:     _inherit = 'product.document'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/crm_team.py:
  Line 10:     _inherit = 'crm.team'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/mail_scheduled_message.py:
  Line 9:     _inherit = 'mail.scheduled.message'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/account_move.py:
  Line 10:     _inherit = ['account.move', 'utm.mixin']


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/res_partner.py:
  Line 9:     _inherit = 'res.partner'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/payment_provider.py:
  Line 8:     _inherit = 'payment.provider'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/ir_config_parameter.py:
  Line 8:     _inherit = 'ir.config_parameter'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/payment_transaction.py:
  Line 11:     _inherit = 'payment.transaction'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/sale/models/sale_order_line.py:
  Line 16: class SaleOrderLine(models.Model):

  Line 17:     _name = 'sale.order.line'

  Line 18:     _inherit = 'analytic.mixin'

```

---

## Assistant (Odoo-Dev · GLM-5.2 · 3.4s)

_Thinking:_

So I've confirmed:

- `fleet.vehicle`, `fleet.vehicle.model`, `fleet.vehicle.log.contract`,
  `fleet.vehicle.log.services` all inherit `mail.thread` and `mail.activity.mixin`
- `sale.order` inherits `mail.thread`, `mail.activity.mixin`

Now let me check the `mail.thread` mixin to see how it connects to `ir.attachment`. Also
let me check purchase.

**Tool: grep**

**Input:**

```json
{
  "path": "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/purchase/models/purchase_order.py",
  "pattern": "class PurchaseOrder|_name = ['\\\"]purchase.order|_inherit"
}
```

**Output:**

```
Found 19 matches
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/purchase/models/res_config_settings.py:
  Line 8:     _inherit = 'res.config.settings'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/purchase/models/analytic_account.py:
  Line 8:     _inherit = 'account.analytic.account'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/purchase/models/res_company.py:
  Line 7:     _inherit = 'res.company'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/purchase/models/account_tax.py:
  Line 7:     _inherit = "account.tax"


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/purchase/models/res_partner.py:
  Line 9:     _inherit = 'res.partner'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/purchase/models/analytic_applicability.py:
  Line 7:     _inherit = 'account.analytic.applicability'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/purchase/models/account_invoice.py:
  Line 17:     _inherit = 'account.move'

  Line 519:     _inherit = 'account.move.line'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/purchase/models/purchase_order_line.py:
  Line 12: class PurchaseOrderLine(models.Model):

  Line 13:     _name = 'purchase.order.line'

  Line 14:     _inherit = 'analytic.mixin'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/purchase/models/ir_actions_report.py:
  Line 8:     _inherit = 'ir.actions.report'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/purchase/models/purchase_order.py:
  Line 18: class PurchaseOrder(models.Model):

  Line 19:     _name = "purchase.order"

  Line 20:     _inherit = ['portal.mixin', 'product.catalog.mixin', 'mail.thread', 'mail.activity.mixin']


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/purchase/models/product.py:
  Line 13:     _inherit = 'product.template'

  Line 65:     _inherit = 'product.product'

  Line 125:     _inherit = "product.supplierinfo"

  Line 137:     _inherit = 'product.packaging'

```

**Tool: grep**

**Input:**

```json
{
  "path": "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_thread.py",
  "pattern": "_name = ['\\\"]mail.thread|class MailThread|message_main_attachment_id|attachment_ids|attachment_id"
}
```

**Output:**

```
Found 100 matches (more matches available)
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_scheduled_message.py:
  Line 39:     attachment_ids = fields.Many2many(

  Line 41:         'scheduled_message_id', 'attachment_id',

  Line 84:             if attachments := scheduled_message.attachment_ids:

  Line 187:                     attachment_ids=list(scheduled_message.attachment_ids.ids),

  Line 284:             data['attachment_ids'] = Store.many(scheduled_message.attachment_ids)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_thread_blacklist.py:
  Line 29:     _name = 'mail.thread.blacklist'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_activity_mixin.py:
  Line 447:     def activity_feedback(self, act_type_xmlids, user_id=None, feedback=None, attachment_ids=None):

  Line 460:             activities.action_feedback(feedback=feedback, attachment_ids=attachment_ids)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_thread_main_attachment.py:
  Line 11:     _name = 'mail.thread.main.attachment'

  Line 15:     message_main_attachment_id = fields.Many2one(string="Main Attachment", comodel_name='ir.attachment', copy=False, index='btree_not_null')

  Line 20:         self.sudo()._message_set_main_attachment_id(

  Line 23:                 for attachment_command in (msg_values['attachment_ids'] or [])

  Line 27:     def _message_set_main_attachment_id(self, attachments, force=False, filter_xml=True):

  Line 38:         if attachments and (force or not self.message_main_attachment_id):

  Line 47:                 self.with_context(tracking_disable=True).message_main_attachment_id = max(

  Line 57:                 {"mainAttachment": Store.one(self.message_main_attachment_id, only_id=True)},


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_message.py:
  Line 101:     attachment_ids = fields.Many2many(

  Line 103:         'message_id', 'attachment_id',

  Line 653:             if not values.get('attachment_ids'):

  Line 654:                 values['attachment_ids'] = []

  Line 675:                             values['attachment_ids'].append((4, attachment.id))

  Line 689:         doc_to_attachment_ids = defaultdict(set)

  Line 692:                for command in values['attachment_ids']):

  Line 694:                 message_attachment_ids = set()

  Line 695:                 for command in values['attachment_ids']:

  Line 697:                         message_attachment_ids.add(command)

  Line 699:                         message_attachment_ids |= set(command[2])

  Line 701:                         message_attachment_ids.add(command[1])

  Line 702:                 if message_attachment_ids:

  Line 704:                     doc_to_attachment_ids[key] |= message_attachment_ids

  Line 706:             attachment_ids_all = {

  Line 707:                 attachment_id

  Line 708:                 for doc_attachment_ids in doc_to_attachment_ids

  Line 709:                 for attachment_id in doc_attachment_ids

  Line 711:             AttachmentSudo = self.env['ir.attachment'].sudo().with_prefetch(list(attachment_ids_all))

  Line 712:             for (model, res_id), doc_attachment_ids in doc_to_attachment_ids.items():

  Line 715:                 attachments_tocheck += AttachmentSudo.browse(doc_attachment_ids).filtered(

  Line 719:             attachments_tocheck = messages.attachment_ids  # fallback on read if any unknown command

  Line 768:         if vals.get('attachment_ids'):

  Line 770:                 mail.attachment_ids.check(mode='read')

  Line 783:         self.mapped('attachment_ids').filtered(

  Line 1076:                 "attachment_ids": Store.many(message.sudo().attachment_ids.sorted("id")),

  Line 1150:                 [("attachment_ids", "in", self.env["ir.attachment"].sudo()._search([("name", "ilike", search_term)]))],

  Line 1268:             and not self.attachment_ids


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_thread_cc.py:
  Line 8:     _name = 'mail.thread.cc'


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_mail.py:
  Line 53:     unrestricted_attachment_ids = fields.Many2many('ir.attachment', string='Unrestricted Attachments',

  Line 54:         compute='_compute_restricted_attachments', inverse='_inverse_unrestricted_attachment_ids')

  Line 104:     @api.depends('attachment_ids')

  Line 112:             mail.unrestricted_attachment_ids = IrAttachment._filter_attachment_access(mail_sudo.attachment_ids.ids)

  Line 113:             mail.restricted_attachment_count = len(mail_sudo.attachment_ids) - len(mail.unrestricted_attachment_ids)

  Line 115:     def _inverse_unrestricted_attachment_ids(self):

  Line 119:             restricted_attaments = mail_sudo.attachment_ids - IrAttachment._filter_attachment_access(mail_sudo.attachment_ids.ids)

  Line 120:             mail_sudo.attachment_ids = restricted_attaments | mail.unrestricted_attachment_ids

  Line 158:             if values.get('attachment_ids'):

  Line 161:             new_mails_w_attach.mapped('attachment_ids').check(mode='read')

  Line 170:         if vals.get('attachment_ids'):

  Line 172:                 mail.attachment_ids.check(mode='read')

  Line 477:         attachments = self.attachment_ids


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_activity.py:
  Line 87:     attachment_ids = fields.Many2many(

  Line 89:         'activity_id', 'attachment_id',

  Line 477:     def action_feedback(self, feedback=False, attachment_ids=None):

  Line 480:         )._action_done(feedback=feedback, attachment_ids=attachment_ids)

  Line 488:     def action_feedback_schedule_next(self, feedback=False, attachment_ids=None):

  Line 496:         _messages, next_activities = self._action_done(feedback=feedback, attachment_ids=attachment_ids)  # will unlink activity, dont access self after that

  Line 509:     def _action_done(self, feedback=False, attachment_ids=None):

  Line 513:             :param attachment_ids: list of ir.attachment ids to attach to the posted mail.message

  Line 549:                         attachment_ids=attachment_ids,

  Line 563:                     attachment_ids = (attachment_ids or []) + activity_attachments.get(activity.id, [])

  Line 564:                     if attachment_ids:

  Line 565:                         activity.attachment_ids = attachment_ids

  Line 577:                         activity_message.attachment_ids = message_attachments

  Line 641:             data["attachment_ids"] = Store.many(activity.attachment_ids, fields=["name"])

  Line 699:             attachment_ids = all_completed.attachment_ids.ids

  Line 702:                 for a in self.env['ir.attachment'].search_read([['id', 'in', attachment_ids]], ['create_date', 'name'])

  Line 703:             } if attachment_ids else {}

  Line 739:             attachments = [attachments_by_id[attach.id] for attach in completed.attachment_ids]


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_template.py:
  Line 68:     attachment_ids = fields.Many2many('ir.attachment', 'email_template_attachment_rel', 'email_template_id',

  Line 69:                                       'attachment_id', 'Attachments',

  Line 173:             record.attachment_ids.write({'res_model': record._name, 'res_id': record.id})

  Line 231:         copy_attachments = 'attachment_ids' not in default

  Line 233:             default['attachment_ids'] = False

  Line 240:                 if original.attachment_ids:

  Line 242:                         'attachment_ids': [

  Line 244:                                 attachment.copy(default={'res_id': copy.id, 'res_model': original._name}) for attachment in original.attachment_ids

  Line 294:           are specific to attachments, e.g. attachment_ids or report_template_ids;

  Line 313:             if 'attachment_ids' in render_fields:

  Line 314:                 values['attachment_ids'] = self.attachment_ids.ids

  Line 352:                 if additional_attachments.get('attachment_ids'):

  Line 353:                     render_results[res_id].setdefault('attachment_ids', []).extend(additional_attachments['attachment_ids'])

  Line 539:             'attachment_ids',  # attachments

  Line 590:             if render_fields_set & {'attachment_ids', 'report_template_ids'}:

  Line 668:                 ('attachment_ids',

  Line 700:                 values['attachment_ids'] = [(4, aid) for aid in (values.get('attachment_ids') or [])]

  Line 763:                     mail.with_context(default_type=None).write({'attachment_ids': attachments_values})


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/ir_attachment.py:
  Line 29:                         message_sudo = self.env['mail.message'].sudo().search([('attachment_ids', 'in', attachment_sudo.ids)], limit=1)

  Line 54:             if not hasattr(related_records, '_message_set_main_attachment_id'):

  Line 61:                     related_record._message_set_main_attachment_id(attachment, force=force)


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/discuss/discuss_voice_metadata.py:
  Line 10:     attachment_id = fields.Many2one(


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_thread.py:
  Line 63: class MailThread(models.AbstractModel):

  Line 100:     _name = 'mail.thread'


(Results truncated. Consider using a more specific path or pattern.)
```

---

## Assistant (Odoo-Dev · GLM-5.2 · 3.3s)

_Thinking:_

Now I have a clear picture. Let me also look at the mail.thread to confirm how
attachments are linked, and check the ir_attachment views to understand what's available
out of the box for viewing attachments.

Let me also confirm the OCA knowledge modules - there's `document_knowledge` which is
the OCA backport of the Knowledge/Documents app. Let me check what these do.

**Tool: read**

**Input:**

```json
{
  "filePath": "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_thread.py",
  "limit": 40,
  "offset": 63
}
```

**Output:**

```
<path>/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/addons/mail/models/mail_thread.py</path>
<type>file</type>
<content>
63: class MailThread(models.AbstractModel):
64:     ''' mail_thread model is meant to be inherited by any model that needs to
65:         act as a discussion topic on which messages can be attached. Public
66:         methods are prefixed with ``message_`` in order to avoid name
67:         collisions with methods of the models that will inherit from this class.
68:
69:         ``mail.thread`` defines fields used to handle and display the
70:         communication history. ``mail.thread`` also manages followers of
71:         inheriting classes. All features and expected behavior are managed
72:         by mail.thread. Widgets has been designed for the 7.0 and following
73:         versions of Odoo.
74:
75:         Inheriting classes are not required to implement any method, as the
76:         default implementation will work for any model. However it is common
77:         to override at least the ``message_new`` and ``message_update``
78:         methods (calling ``super``) to add model-specific behavior at
79:         creation and update of a thread when processing incoming emails.
80:
81:         Options:
82:             - _mail_flat_thread: if set to True, all messages without parent_id
83:                 are automatically attached to the first message posted on the
84:                 resource. If set to False, the display of Chatter is done using
85:                 threads, and no parent_id is automatically set.
86:
87:     MailThread features can be somewhat controlled through context keys :
88:
89:      - ``mail_create_nosubscribe``: at create or message_post, do not subscribe
90:        uid to the record thread
91:      - ``mail_create_nolog``: at create, do not log the automatic '<Document>
92:        created' message
93:      - ``mail_notrack``: at create and write, do not perform the value tracking
94:        creating messages
95:      - ``tracking_disable``: at create and write, perform no MailThread features
96:        (auto subscription, tracking, post, ...)
97:      - ``mail_notify_force_send``: if less than 50 email notifications to send,
98:        send them directly instead of using the queue; True by default
99:     '''
100:     _name = 'mail.thread'
101:     _description = 'Email Thread'
102:     _mail_flat_thread = True  # flatten the discussion history

(Showing lines 63-102 of 4830. Use offset=103 to continue.)
</content>
```

**Tool: bash**

**Input:**

```json
{
  "command": "ls /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_knowledge/ 2>/dev/null; echo \"---manifest---\"; cat /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_knowledge/__manifest__.py 2>/dev/null",
  "description": "Inspect document_knowledge OCA module"
}
```

**Output:**

```
data
demo
i18n
__init__.py
__manifest__.py
models
pyproject.toml
readme
README.rst
security
static
views
---manifest---
# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Documents Knowledge",
    "version": "18.0.1.0.2",
    "author": "OpenERP SA,"
    "MONK Software, "
    "Tecnativa, "
    "ForgeFlow, "
    "Odoo Community Association (OCA)",
    "category": "Knowledge",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/knowledge",
    "depends": ["base"],
    "data": [
        "data/ir_module_category.xml",
        "security/document_knowledge_security.xml",
        "data/res_users.xml",
        "views/document_knowledge.xml",
        "views/res_config.xml",
    ],
    "demo": ["demo/document_knowledge.xml"],
    "installable": True,
    "application": True,
}

```

---

## Assistant (Odoo-Dev · GLM-5.2 · 3.3s)

**Tool: bash**

**Input:**

```json
{
  "command": "ls /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_knowledge/models/; echo \"---model file---\"; cat /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_knowledge/models/*.py 2>/dev/null | head -120",
  "description": "Inspect document_knowledge models"
}
```

**Output:**

```
__init__.py
ir_attachment.py
res_config.py
---model file---
# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from . import ir_attachment
from . import res_config
# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    # Add index to res_model because filtering on it is a common use case
    res_model = fields.Char(index=True)
# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class DocumentKnowledgeConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_ir_attachment_user = fields.Boolean(
        string="Central access to Documents",
        implied_group="document_knowledge.group_ir_attachment_user",
    )

```

**Tool: grep**

**Input:**

```json
{
  "path": "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/views/ir_attachment_views.xml",
  "pattern": "ir.attachment|act_window|menuitem|kanban|list|form"
}
```

**Output:**

```
Found 100 matches (more matches available)
/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/views/res_device_views.xml:
  Line 5:         <record model="ir.ui.view" id="res_device_view_form">

  Line 6:             <field name="name">res.device.form</field>

  Line 9:                 <form>

  Line 24:                 </form>

  Line 29:             <field name="name">res.device.list</field>

  Line 32:                 <list default_order="last_activity desc">

  Line 41:                 </list>

  Line 45:         <record model="ir.ui.view" id="res_device_view_kanban">

  Line 46:             <field name="name">res.device.kanban</field>

  Line 49:                 <kanban create="false" default_order="is_current desc, last_activity desc">

  Line 77:                 </kanban>

  Line 81:         <record id="action_user_device" model="ir.actions.act_window">

  Line 85:             <field name="view_mode">list,kanban,form</field>

  Line 87:         <menuitem action="action_user_device" id="menu_action_user_device" parent="base.menu_security" sequence="10"/>


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/views/res_currency_views.xml:
  Line 15:             <field name="name">res.currency.rate.list</field>

  Line 18:                 <list string="Currency Rates" editable="bottom">

  Line 25:                 </list>

  Line 29:         <record id="view_currency_rate_form" model="ir.ui.view">

  Line 30:             <field name="name">res.currency.rate.form</field>

  Line 33:                 <form string="Currency Rate">

  Line 48:                 </form>

  Line 52:         <record id="act_view_currency_rates" model="ir.actions.act_window">

  Line 55:             <field name='view_mode'>list,form</field>

  Line 61:             <field name="binding_view_types">form</field>

  Line 83:             <field name="name">res.currency.list</field>

  Line 86:                 <list string="Currencies" decoration-muted="(not active)">

  Line 94:                 </list>

  Line 98:         <record id="view_currency_kanban" model="ir.ui.view">

  Line 99:             <field name="name">res.currency.kanban</field>

  Line 102:                 <kanban class="o_kanban_mobile">

  Line 125:                 </kanban>

  Line 129:         <record id="view_currency_form" model="ir.ui.view">

  Line 130:             <field name="name">res.currency.form</field>

  Line 133:                 <form string="Currency">

  Line 164:                         <notebook class="o_currency_rate_list" invisible="is_current_company_currency">

  Line 167:                                     <list string="Rates"  editable="top" limit="25">

  Line 174:                                     </list>

  Line 179:                 </form>

  Line 183:         <record id="action_currency_form" model="ir.actions.act_window">

  Line 186:             <field name="view_mode">list,kanban,form</field>


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/views/res_bank_views.xml:
  Line 5:         <record id="view_res_bank_form" model="ir.ui.view">

  Line 6:             <field name="name">res.bank.form</field>

  Line 9:                 <form string="Bank">

  Line 19:                                 <div class="o_address_format">

  Line 34:                 </form>

  Line 39:             <field name="name">res.bank.list</field>

  Line 42:                 <list string="Banks">

  Line 46:                 </list>

  Line 62:         <record id="action_res_bank_form" model="ir.actions.act_window">

  Line 65:             <field name="view_mode">list,form</field>

  Line 76:         <record id="view_partner_bank_form" model="ir.ui.view">

  Line 77:             <field name="name">res.partner.bank.form</field>

  Line 81:                 <form string="Bank account" name="bank_account_form">

  Line 101:                 </form>

  Line 106:             <field name="name">res.partner.bank.list</field>

  Line 109:                 <list string="Bank Accounts" multi_edit="1" decoration-muted="(not active)">

  Line 117:                 </list>

  Line 135:         <record id="action_res_partner_bank_account_form" model="ir.actions.act_window">

  Line 138:             <field name="view_mode">list,form</field>


/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/views/res_users_views.xml:
  Line 4:         <record id="change_password_own_form" model="ir.ui.view">

  Line 8:                 <form string="Change Password">

  Line 17:                 </form>

  Line 26:                 <form string="Change Password">

  Line 27:                     <field mode="list" name="user_ids"/>

  Line 32:                 </form>

  Line 39:                 <!-- the user list is editable, but one cannot add or delete rows -->

  Line 40:                 <list string="Users" editable="bottom" create="false" delete="false">

  Line 44:                 </list>

  Line 47:         <record id="change_password_wizard_action" model="ir.actions.act_window">

  Line 50:             <field name="view_mode">form</field>

  Line 68:         <record id="view_groups_form" model="ir.ui.view">

  Line 69:             <field name="name">res.groups.form</field>

  Line 72:                 <form string="Groups">

  Line 96:                                 <list string="Access Rights" editable="top">

  Line 103:                                 </list>

  Line 108:                                 <list string="Record Rules" editable="top">

  Line 116:                                 </list>

  Line 123:                 </form>

  Line 126:         <record id="action_res_groups" model="ir.actions.act_window">

  Line 129:             <field name="context">{'search_default_filter_no_share': 1, 'ir.ui.menu.full_list': 1}</field>

  Line 132:         <menuitem action="action_res_groups" id="menu_action_res_groups" parent="base.menu_users" groups="base.group_no_one" sequence="3"/>

  Line 135:         <record id="view_users_simple_form" model="ir.ui.view">

  Line 136:             <field name="name">res.users.simplified.form</field>

  Line 140:                 <form string="Users">

  Line 167:                 </form>

  Line 170:         <record id="view_users_form" model="ir.ui.view">

  Line 171:             <field name="name">res.users.form</field>

  Line 174:                 <form string="Users">

  Line 182:                             <button name="action_show_accesses" type="object" groups="base.group_no_one" class="oe_stat_button" icon="fa-list">

  Line 185:                             <button name="action_show_rules" type="object" groups="base.group_no_one" class="oe_stat_button" icon="fa-list-ul">

  Line 190:                         <div class="alert alert-info text-center o_form_header"

  Line 251:                 </form>

  Line 256:             <field name="name">res.users.list</field>

  Line 259:                 <list string="Users" multi_edit="1">

  Line 265:                 </list>

  Line 268:         <record id="view_res_users_kanban" model="ir.ui.view">

  Line 269:             <field name="name">res.users.kanban</field>

  Line 272:                 <kanban class="o_kanban_mobile">

  Line 300:                 </kanban>

  Line 321:             <field name="inherit_id" ref="view_users_form"/>


(Results truncated. Consider using a more specific path or pattern.)
```

---

## Assistant (Odoo-Dev · GLM-5.2 · 4.2s)

**Tool: read**

**Input:**

```json
{
  "filePath": "/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/views/ir_attachment_views.xml"
}
```

**Output:**

```
<path>/home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/odoo/odoo/addons/base/views/ir_attachment_views.xml</path>
<type>file</type>
<content>
1: <?xml version="1.0" encoding="utf-8"?>
2: <odoo>
3:         <!-- Attachment -->
4:         <record id="view_attachment_form" model="ir.ui.view">
5:             <field name="model">ir.attachment</field>
6:             <field name="arch" type="xml">
7:                 <form string="Attachments">
8:                    <sheet>
9:                     <label for="name"/>
10:                     <h1>
11:                         <field name="name"/>
12:                     </h1>
13:                     <group>
14:                         <group class="w-100">
15:                             <field name="type"/>
16:                             <label for="datas" class="mt-1" invisible="type == 'url'"/>
17:                             <field name="datas" nolabel="1" class="w-100" filename="name" invisible="type == 'url'"/>
18:                             <field name="url" widget="url" invisible="type == 'binary'"/>
19:                             <field name="mimetype" groups="base.group_no_one"/>
20:                         </group>
21:                         <group string="Attached To" groups="base.group_no_one">
22:                             <field name="res_model"/>
23:                             <field name="res_field"/>
24:                             <field name="res_id"/>
25:                             <field name="res_name"/>
26:                             <field name="company_id" groups="base.group_multi_company" options="{'no_create': True}"/>
27:                             <field name="public"/>
28:                         </group>
29:                         <group string="History" groups="base.group_no_one" invisible="not create_date">
30:                             <label for="create_uid" string="Creation"/>
31:                             <div name="creation_div">
32:                                 <field name="create_uid" readonly="1" class="oe_inline"/> on
33:                                 <field name="create_date" readonly="1" class="oe_inline"/>
34:                             </div>
35:                         </group>
36:                         <group name="description_group" string="Description" groups="base.group_no_one" colspan="4">
37:                             <field name="description" nolabel="1"/>
38:                         </group>
39:                         <group groups="base.group_no_one" string="Indexed Content" colspan="4">
40:                             <field name="index_content" nolabel="1"/>
41:                         </group>
42:                     </group>
43:                   </sheet>
44:                 </form>
45:             </field>
46:         </record>
47:         <record id="view_attachment_tree" model="ir.ui.view">
48:             <field name="model">ir.attachment</field>
49:             <field name="arch" type="xml">
50:                 <list string="Attachments">
51:                     <field name="name"/>
52:                     <field name="res_model"/>
53:                     <field name="res_field"/>
54:                     <field name="res_id"/>
55:                     <field name="type"/>
56:                     <field name="file_size"/>
57:                     <field name="company_id" groups="base.group_multi_company"/>
58:                     <field name="create_uid"/>
59:                     <field name="create_date"/>
60:                 </list>
61:             </field>
62:         </record>
63:         <record id="view_attachment_search" model="ir.ui.view">
64:             <field name="model">ir.attachment</field>
65:             <field name="arch" type="xml">
66:                 <search string="Attachments">
67:                     <field name="name" filter_domain="[('name','ilike',self)]" string="Attachment"/>
68:                     <field name="create_date"/>
69:                     <filter name="my_documents_filter"
70:                         string="My Document(s)"
71:                         domain="[('create_uid','=',uid)]"
72:                         help="Filter on my documents"/>
73:                     <filter name="url_filter" string="URL" domain="[('type', '=', 'url')]"/>
74:                     <filter name="binary_filter" string="Stored" domain="[('type', '=', 'binary')]"/>
75:                     <separator/>
76:                     <field name="create_uid" string="Created by"/>
77:                     <field name="type"/>
78:                     <group expand="0" string="Group By">
79:                         <filter name="owner" string="Owner" domain="[]" context="{'group_by':'create_uid'}"/>
80:                         <filter string="Type" name="type" domain="[]" context="{'group_by':'type'}" groups="base.group_no_one"/>
81:                         <filter string="Company" name="company" domain="[]" context="{'group_by':'company_id'}" groups="base.group_multi_company"/>
82:                         <filter string="Creation Date" name="creation_month" domain="[]" context="{'group_by':'create_date'}"/>
83:                     </group>
84:                 </search>
85:             </field>
86:         </record>
87:         <record id="action_attachment" model="ir.actions.act_window">
88:             <field name="name">Attachments</field>
89:             <field name="res_model">ir.attachment</field>
90:             <field name="view_id" eval="False"/>
91:             <field name="search_view_id" ref="view_attachment_search"/>
92:             <field name="help" type="html">
93:                 <p class="o_view_nocontent_smiling_face">
94:                     Create a new document
95:                 </p>
96:                 <p>
97:                     Also you will find here all the related documents and download it by clicking on any individual document.
98:                 </p>
99:             </field>
100:         </record>
101:         <menuitem action="action_attachment" id="menu_action_attachment" parent="base.next_id_9"/>
102:
103: </odoo>

(End of file - total 103 lines)
</content>
```

---

## Assistant (Odoo-Dev · GLM-5.2 · 2.5s)

_Thinking:_

Now let me check the document_knowledge views to see if it provides a centralized way to
view attachments.

**Tool: bash**

**Input:**

```json
{
  "command": "cat /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/document_knowledge/views/document_knowledge.xml",
  "description": "Inspect document_knowledge views"
}
```

**Output:**

```
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <record id="knowledge_action_documents" model="ir.actions.act_window">
        <field name="name">Documents</field>
        <field name="path">knowledge-documents</field>
        <field name="res_model">ir.attachment</field>
        <field name="view_mode">kanban,list,form</field>
        <field name="context">{'search_default_user_documents': True}</field>
    </record>
    <record id="ir_attachment_view_user_documents" model="ir.ui.view">
        <field name="name">Documents search view: additional filters</field>
        <field name="model">ir.attachment</field>
        <field name="inherit_id" ref="base.view_attachment_search" />
        <field name="arch" type="xml">
            <search>
                <field name="res_model" />
                <field name="index_content" />
                <filter
                    name="user_documents"
                    string="Documents"
                    domain="[('res_model', 'not like', 'ir.%'), ('res_model', '!=', False)]"
                />
                <group string="Group by">
                    <filter
                        name="group_model"
                        string="Model"
                        context="{'group_by': 'res_model'}"
                    />
                </group>
            </search>
        </field>
    </record>
    <!-- Top menu item -->
    <menuitem
        id="menu_document_root"
        name="Knowledge"
        groups="document_knowledge.group_document_user"
        web_icon="document_knowledge,static/description/icon.png"
        sequence="116"
    />
    <menuitem
        id="menu_document_section"
        name="Documents"
        groups="document_knowledge.group_ir_attachment_user"
        parent="menu_document_root"
        sequence="150"
    />
    <menuitem
        id="menu_document"
        name="Documents"
        action="knowledge_action_documents"
        parent="menu_document_section"
        sequence="0"
    />
</odoo>

```

**Tool: bash**

**Input:**

```json
{
  "command": "ls /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/; echo \"---attachment modules?---\"; ls /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/oca/knowledge/ | grep -i -E \"attach|document\"",
  "description": "List knowledge OCA modules"
}
```

**Output:**

```
attachment_preview
attachment_zipped_download
checklog-odoo.cfg
document_knowledge
document_page
document_page_access_group
document_page_access_group_user_role
document_page_approval
document_page_group
document_page_partner
document_page_product
document_page_project
document_page_project_task
document_page_reference
document_page_tag
document_url
eslint.config.cjs
LICENSE
prettier.config.cjs
README.md
setup
test-requirements.txt
---attachment modules?---
attachment_preview
attachment_zipped_download
document_knowledge
document_page
document_page_access_group
document_page_access_group_user_role
document_page_approval
document_page_group
document_page_partner
document_page_product
document_page_project
document_page_project_task
document_page_reference
document_page_tag
document_url

```

---

## Assistant (Odoo-Dev · GLM-5.2 · 4.9s)

_Thinking:_

I now have everything I need. Let me also check the socger_hospital module to see if it
uses mail.thread, and verify the addons.yaml to confirm knowledge is included.

Let me check the addons.yaml to confirm what's available.

**Tool: bash**

**Input:**

```json
{
  "command": "cat /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/addons.yaml; echo \"---repos---\"; cat /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/src/repos.yaml",
  "description": "Check aggregated addons and repos"
}
```

**Output:**

```
oca/bank-payment:
  - "*"
oca/community-data-files:
  - "*"
oca/knowledge:
  - "*"
oca/l10n-spain:
  - "*"
oca/web:
  - "*"
# muk/base:
#   - "*"
# muk/web:
#   - "*"

# libreinnova/crm:
#   - "*"
# libreinnova/custom:
#   - "*"
---repos---
# See https://github.com/Tecnativa/doodba#optodoocustomsrcreposyaml
./odoo:
  defaults:
    # Shallow repositories ($DEPTH_DEFAULT=1) are faster & thinner
    # You may need a bigger depth when merging PRs (use $DEPTH_MERGE
    # for a sane value of 100 commits)
    depth: $DEPTH_DEFAULT
  remotes:
    ocb: https://github.com/OCA/OCB.git
    odoo: https://github.com/odoo/odoo.git
    openupgrade: https://github.com/OCA/OpenUpgrade.git
  target: ocb $ODOO_VERSION
  merges:
    - ocb $ODOO_VERSION
    # Example of a merge of the PR with the number <PR>
    # - oca refs/pull/<PR>/head
# +----------------------------+
# | Repositorio público Muk IT |
# | No tiene rama para Odoo 18 |
# +----------------------------+
# ./muk/base:
#   defaults:
#     depth: $DEPTH_DEFAULT
#   remotes:
#     origin: https://github.com/muk-it/muk_base.git
#   target: origin $ODOO_VERSION
#   merges:
#     - origin $ODOO_VERSION

# ./muk/web:
#   defaults:
#     depth: $DEPTH_DEFAULT
#   remotes:
#     origin: https://github.com/muk-it/muk_web.git
#   target: origin $ODOO_VERSION
#   merges:
#     - origin $ODOO_VERSION

# +----------------------------+
# | Repositorio privado        |
# | Requiere configuración SSH |
# +----------------------------+
# ./libreinnova/plf:
#   defaults:
#     depth: $DEPTH_DEFAULT
#   remotes:
#     origin: git+ssh://git@bitbucket.org/galvintec/odoo_libreinnova_plf_addons.git
#   target: origin $ODOO_VERSION
#   merges:
#     - origin $ODOO_VERSION

```

---

## Assistant (Odoo-Dev · GLM-5.2 · 63.1s)

_Thinking:_

I have all the information I need. Let me put together a clear, complete answer in
Spanish.

Summary of what I found:

1. **Tabla principal donde se guardan TODOS los documentos**: `ir_attachment` (modelo
   `ir.attachment`)

   - Definida en `odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment.py`
   - Es el repositorio ÚNICO y centralizado para TODOS los adjuntos de Odoo
   - Campos clave:
     - `name` — nombre del fichero
     - `res_model` — modelo al que está vinculado (Char, no FK)
     - `res_id` — ID del registro al que está vinculado (Many2oneReference)
     - `res_field` — campo específico (para campos Binary almacenados como attachment)
     - `res_name` — nombre calculado del recurso vinculado
     - `type` — 'url' o 'binary'
     - `datas` — contenido base64 (computed)
     - `raw` — contenido binario (computed)
     - `db_datas` — contenido binario almacenado en BD (cuando storage=db)
     - `store_fname` — ruta relativa en el filestore (cuando storage=file)
     - `file_size`, `checksum` (SHA1), `mimetype`, `index_content` (texto indexado para
       búsqueda)
     - `url`, `public`, `access_token`, `company_id`
   - Almacenamiento físico: depende del parámetro `ir_attachment.location` (por defecto
     'file' → filestore en disco; puede ser 'db' → en la columna `db_datas`)
   - Index creado: `ir_attachment_res_idx` sobre `(res_model, res_id)`

2. **Cómo se asocian los adjuntos a los modelos de negocio (Flota, Ventas, Compras,
   etc.)**:

   - Todos esos modelos heredan el mixin `mail.thread` (y normalmente
     `mail.activity.mixin`):
     - `fleet.vehicle` →
       `_inherit = ['mail.thread', 'mail.activity.mixin', 'avatar.mixin']`
     - `fleet.vehicle.model` → `['mail.thread', 'mail.activity.mixin', 'avatar.mixin']`
     - `fleet.vehicle.log.contract` → `['mail.thread', 'mail.activity.mixin']`
     - `fleet.vehicle.log.services` → `['mail.thread', 'mail.activity.mixin']`
     - `sale.order` →
       `['portal.mixin', 'product.catalog.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']`
     - `purchase.order` →
       `['portal.mixin', 'product.catalog.mixin', 'mail.thread', 'mail.activity.mixin']`
   - El mixin `mail.thread` añade el chatter y gestiona los adjuntos a través de
     `mail.message.attachment.rel` (tabla M2M entre `mail.message` e `ir.attachment`)
   - Existe `mail.thread.main.attachment` mixin con el campo
     `message_main_attachment_id` (Many2one a `ir.attachment`) — el "adjunto principal"
     del registro

3. **Tablas relacionadas involucradas**:

   - `ir_attachment` — los adjuntos en sí (lo que pregunta el usuario)
   - `mail_message` — los mensajes del chatter
   - `mail_message_res_partner_needaction_rel`, `mail_message_mail_followers_read` etc.
     — relaciones del chatter
   - La relación M2M `mail.message ↔ ir.attachment` se define en `mail_message.py` línea
     101-103 con tabla relacional automática (`message_id`, `attachment_id`)
   - `message_main_attachment_id` es un Many2one directo en `ir.attachment`

4. **Módulos para ver todos los documentos guardados**:

   - **Odoo Enterprise**: la app `documents` (no disponible aquí, es Enterprise) — app
     completa de gestión documental con tags, flujos de aprobación, OCR, etc.
   - **OCA Knowledge** (YA agregado en este proyecto vía `addons.yaml` con
     `oca/knowledge: ["*"]`): el módulo **`document_knowledge`** ofrece exactamente lo
     que pide el usuario:
     - Acción `knowledge_action_documents` sobre `ir.attachment` con vistas
       kanban/list/form
     - Filtro `user_documents` que excluye los internos (`res_model not like 'ir.%'`)
     - Agrupación por `res_model` (es decir, ver documentos agrupados por el modelo al
       que pertenecen)
     - Menú "Knowledge → Documents"
     - Añade índice a `res_model` para acelerar las búsquedas cruzadas
     - Settings para dar "acceso central a Documentos" (grupo
       `group_ir_attachment_user`)
   - **Base (Odoo core)**: ya de fábrica existe la acción `base.action_attachment` y el
     menú `base.menu_action_attachment` (bajo Settings → Technical → ... → Attachments),
     pero está pensado para admins/desarrolladores, con la vista search filtrable por
     `name`, `create_uid`, `type`, etc. Es menos user-friendly que `document_knowledge`.
   - Otros módulos OCA útiles del mismo repo `oca/knowledge` ya disponibles:
     `attachment_preview`, `attachment_zipped_download`, `document_url`, y la familia
     `document_page_*` (páginas wiki-like).

5. **Dónde físicamente se guardan**:
   - Por defecto (`ir_attachment.location = 'file'`): en el **filestore** del disco, en
     el contenedor sería `/var/lib/odoo/filestore/<dbname>/` (subdirectorios `XX/<sha1>`
     basados en el hash SHA1 del contenido; scatter en 256 dirs)
   - Si se configura `ir_attachment.location = 'db'`: en la columna `db_datas` (bytea)
     de la tabla `ir_attachment`
   - El parámetro se lee en `ir_attachment._storage()` (línea 59-60 del fichero)

Voy a responder con todo esto de forma clara y estructurada. No modificaré nada como
pidió el usuario.

Tengo toda la información necesaria. Aquí va la respuesta detallada sin haber tocado
ningún fichero.

---

# Respuesta: dónde se guardan los documentos y cómo verlos todos

## 1. La tabla única: `ir_attachment` (modelo `ir.attachment`)

**Todos** los documentos que subes a Flota, presupuestos, pedidos, facturas, contactos,
etc. terminan en la **misma** tabla: `ir_attachment`. No hay una tabla por modelo — Odoo
usa un repositorio central y lo enlaza vía dos columnas "polimórficas".

Definición: `odoo/custom/src/odoo/odoo/addons/base/models/ir_attachment.py`

Campos clave (líneas 410–435):

| Campo                                                       | Tipo                     | Significado                                                                        |
| ----------------------------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| `name`                                                      | Char                     | Nombre del fichero                                                                 |
| `res_model`                                                 | Char                     | Modelo al que va vinculado (p.ej. `fleet.vehicle`, `sale.order`, `purchase.order`) |
| `res_id`                                                    | Many2oneReference        | ID del registro de ese modelo                                                      |
| `res_field`                                                 | Char                     | Si el adjunto almacena un campo `Binary` concreto (p.ej. la foto de un contacto)   |
| `res_name`                                                  | Char (compute)           | `display_name` del registro vinculado                                              |
| `type`                                                      | Selection `url`/`binary` | URL o fichero físico                                                               |
| `datas`                                                     | Binary (compute)         | Contenido en base64                                                                |
| `raw`                                                       | Binary (compute)         | Contenido en bytes                                                                 |
| `db_datas`                                                  | Binary                   | Contenido cuando se almacena **en BD**                                             |
| `store_fname`                                               | Char                     | Ruta relativa cuando se almacena **en disco** (`XX/<sha1>`)                        |
| `file_size`, `checksum` (SHA1), `mimetype`, `index_content` | —                        | Metadatos + contenido indexable para búsqueda                                      |
| `public`, `access_token`, `company_id`, `url`               | —                        | Acceso externo / multi-compañía                                                    |

Hay un índice explícito `ir_attachment_res_idx` sobre `(res_model, res_id)` (línea 439)
para acelerar las consultas "dame los adjuntos de este registro".

## 2. Dónde se guarda físicamente el binario

Lo decide el parámetro de sistema `ir_attachment.location` (leído en `_storage()`, línea
59–60):

- **`file` (default)** → en el **filestore** del disco: `filestore/<dbname>/<XX>/<sha1>`
  (se "scatter" en 256 subdirectorios por el hash SHA1 del contenido). Deduplica por
  hash.
- **`db`** → en la columna `db_datas` (tipo `bytea`) de la propia tabla `ir_attachment`.

En este proyecto (Doodba) el filestore vive dentro del contenedor Odoo en
`/var/lib/odoo/filestore/devel/`. No se versiona.

## 3. Cómo se ligan los adjuntos a Flota / Ventas / Compras

Esos modelos **heredan el mixin `mail.thread`** (el que pinta el "chatter" de la derecha
con mensajes y adjuntos). Al heredarlo, cualquier `ir.attachment` subido por el chatter
queda con `res_model = 'fleet.vehicle'` (p.ej.) y `res_id = <id del vehículo>`.
Confirmado en tu código:

- `fleet.vehicle` → `_inherit = ['mail.thread', 'mail.activity.mixin', 'avatar.mixin']`
- `fleet.vehicle.model` → `['mail.thread', 'mail.activity.mixin', 'avatar.mixin']`
- `fleet.vehicle.log.contract` → `['mail.thread', 'mail.activity.mixin']`
- `fleet.vehicle.log.services` → `['mail.thread', 'mail.activity.mixin']`
- `sale.order` →
  `['portal.mixin', 'product.catalog.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']`
- `purchase.order` →
  `['portal.mixin', 'product.catalog.mixin', 'mail.thread', 'mail.activity.mixin']`

Tablas relacionadas con el chatter que también tocan adjuntos:

- `mail_message` → los mensajes del hilo.
- Tabla M2M implícita `mail_message_attachment_rel` (columnas `message_id`,
  `attachment_id`) definida en `mail/models/mail_message.py:101-103` → asocia cada
  mensaje con sus adjuntos.
- `mail.thread.main.attachment` (mixin en `mail/models/mail_thread_main_attachment.py`)
  añade el campo `message_main_attachment_id` (Many2one → `ir.attachment`) que es el
  "adjunto principal" que muestra el chatter.

## 4. ¿Hay un módulo para ver TODOS los documentos, sean del modelo que sean?

**Sí, y ya lo tienes agregado en el proyecto.** Tres opciones, de más a menos potente:

### a) OCA `document_knowledge` (recomendada, ya disponible)

En `odoo/custom/src/addons.yaml` tienes `oca/knowledge: ["*"]`, y el módulo
`document_knowledge` está en `odoo/custom/src/oca/knowledge/document_knowledge/`. Hace
**exactamente** lo que pides:

- Acción `knowledge_action_documents` sobre `ir.attachment` con vistas **kanban / list /
  form**.
- Filtro por defecto `user_documents` con dominio
  `[('res_model', 'not like', 'ir.%'), ('res_model', '!=', False)]` → muestra solo
  adjuntos de negocio, ocultando los técnicos internos.
- **Agrupación por `res_model`** → ves los documentos agrupados por "Flota", "Pedidos de
  venta", etc.
- Añade un índice a la columna `res_model` para acelerar estas búsquedas transversales.
- Menú **Knowledge → Documents** + grupo `group_ir_attachment_user` para dar acceso
  central.
- Settings: "Central access to Documents" para activar el acceso.

Para usarlo: instalar el módulo e instalar también (opcional pero útil)
`attachment_preview` (previsualización en cliente), `attachment_zipped_download`
(descarga en zip), `document_url` (adjuntos tipo URL), todos del mismo repo
`oca/knowledge` ya agregado.

### b) Odoo Enterprise `documents` (no disponible aquí)

Es la app de Documents de pago: tags, flujos de aprobación, OCR, integración con tareas,
hojas de cálculo, etc. No está en este scaffold (no es OCA ni core comunitario).

### c) Lo que ya trae Odoo base (sin instalar nada)

Existe desde el core la acción `base.action_attachment` y el menú
`base.menu_action_attachment` (vistas en
`odoo/custom/src/odoo/odoo/addons/base/views/ir_attachment_views.xml`). Es la vista
"cruda" de `ir.attachment` con búsqueda por nombre, tipo, propietario, fecha y
agrupación por propietario/tipo/compañía/fecha. Funcional pero orientada a
admin/desarrollador (coloca el menú bajo _Settings → Technical_), menos pulida que
`document_knowledge`.

## 5. Resumen ejecutivo

- **Tabla única**: `ir.attachment` (BD: `ir_attachment`); se vincula por las columnas
  `res_model` + `res_id`.
- **Binario**: por defecto en el **filestore del disco** (deduplicado por SHA1),
  alternativamente en la columna `db_datas` si `ir_attachment.location=db`.
- **Por qué aparece en Flota/Ventas/Compras**: esos modelos heredan `mail.thread`, que
  escribe los adjuntos del chatter en `ir.attachment` apuntando a ese modelo/ID.
- **Para verlos todos en una pantalla**: instala **`document_knowledge`** (OCA, ya
  agregado en `addons.yaml`) → menú _Knowledge → Documents_, vista kanban/list agrupable
  por modelo. O, sin instalar nada, usa la acción técnica `base.action_attachment`.

No he modificado ningún fichero, tal y como pediste.

---

## User

Estos documentos que se asocian a modelos, son guardados en la base de datos, o son
guardados en algun path del repositorio?

---

## Assistant (Odoo-Dev · GLM-5.2 · 8.6s)

_Thinking:_

El usuario pregunta si los documentos (adjuntos) que se asocian a modelos se guardan en
la base de datos o en algún path del repositorio. Ya tengo bastante info del análisis
anterior, pero déjame confirmar bien la parte del filestore y dónde vive físicamente en
este proyecto Doodba.

Déjame verificar:

1. El parámetro `ir_attachment.location` por defecto
2. Dónde se configura el filestore en Doodba
3. Confirmar que no es en el repositorio

Voy a revisar la configuración de Doodba para confirmar dónde vive el filestore.

Buena pregunta, importante para entenderlo bien. Déjame verificar cómo está configurado
el almacenamiento en este proyecto Doodba concreto.

**Tool: grep**

**Input:**

```json
{
  "path": "/home/socger/trabajo/galvintec/odoo/tutorial",
  "pattern": "ir_attachment.location|filestore|data_dir|DATA_DIR",
  "include": "*.yaml"
}
```

**Output:**

```
Found 5 matches
/home/socger/trabajo/galvintec/odoo/tutorial/common.yaml:
  Line 17:       - filestore:/var/lib/odoo


/home/socger/trabajo/galvintec/odoo/tutorial/migration.yaml:
  Line 127:   filestore:


/home/socger/trabajo/galvintec/odoo/tutorial/prod.yaml:
  Line 47:   filestore:


/home/socger/trabajo/galvintec/odoo/tutorial/test.yaml:
  Line 127:   filestore:


/home/socger/trabajo/galvintec/odoo/tutorial/devel.yaml:
  Line 154:   filestore:

```

**Tool: grep**

**Input:**

```json
{
  "path": "/home/socger/trabajo/galvintec/odoo/tutorial",
  "pattern": "ir_attachment.location|filestore",
  "include": "*.py"
}
```

**Output:**

```
Found 2 matches
/home/socger/trabajo/galvintec/odoo/tutorial/tasks.py:
  Line 1280:     """Snapshot current database and filestore.

  Line 1313:     """Restore database and filestore snapshot.

```

**Tool: bash**

**Input:**

```json
{
  "command": "ls /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/conf.d/ 2>/dev/null; echo \"---\"; ls /home/socger/trabajo/galvintec/odoo/tutorial/odoo/custom/",
  "description": "Inspect custom conf.d directory"
}
```

**Output:**

```
---
build.d
conf.d
dependencies
entrypoint.d
src
ssh

```

---

## Assistant (Odoo-Dev · GLM-5.2 · 2.3s)

**Tool: read**

**Input:**

```json
{
  "filePath": "/home/socger/trabajo/galvintec/odoo/tutorial/common.yaml",
  "limit": 40
}
```

**Output:**

```
<path>/home/socger/trabajo/galvintec/odoo/tutorial/common.yaml</path>
<type>file</type>
<content>
1: services:
2:   odoo:
3:     build:
4:       context: ./odoo
5:       args:
6:         DB_VERSION: "18"
7:         ODOO_VERSION: "18.0"
8:         UID: "${UID:-1000}"
9:         GID: "${GID:-1000}"
10:     environment:
11:       EMAIL_FROM: ""
12:       PGDATABASE: &dbname prod
13:       PGUSER: &dbuser "odoo"
14:       PROXY_MODE: "true"
15:     tty: true
16:     volumes:
17:       - filestore:/var/lib/odoo
18:     labels:
19:       traefik.backend.buffering.retryExpression: IsNetworkError() && Attempts() < 5
20:       traefik.docker.network: "inverseproxy_shared"
21:       traefik.frontend.passHostHeader: "true"
22:       traefik.port: "8069"
23:
24:   db:
25:     image: ghcr.io/tecnativa/postgres-autoconf:18-alpine
26:     shm_size: 4gb
27:     environment:
28:       POSTGRES_DB: *dbname
29:       POSTGRES_USER: *dbuser
30:       PGDATA: "/var/lib/postgresql/data"
31:       CONF_EXTRA: |
32:         work_mem = 512MB
33:     volumes:
34:       - db:/var/lib/postgresql/data
35:
36:   smtpfake:
37:     image: docker.io/mailhog/mailhog

(End of file - total 37 lines)
</content>
```

**Tool: read**

**Input:**

```json
{
  "filePath": "/home/socger/trabajo/galvintec/odoo/tutorial/devel.yaml",
  "offset": 140,
  "limit": 30
}
```

**Output:**

```
<path>/home/socger/trabajo/galvintec/odoo/tutorial/devel.yaml</path>
<type>file</type>
<content>
140:       whitelist:
141:         aliases:
142:           - proxy_general
143:       public:
144:     environment:
145:       MODE_RUN: "gateway"
146:       ALLOWED_HOSTS: *proxy_allowed_hosts
147: networks:
148:   default:
149:     internal: ${DOODBA_NETWORK_INTERNAL-true}
150:   public:
151:   whitelist:
152:
153: volumes:
154:   filestore:
155:   db:

(End of file - total 155 lines)
</content>
```

---

## Assistant (Odoo-Dev · GLM-5.2 · 32.6s)

_Thinking:_

Perfecto. Confirmado:

1. El volumen Docker `filestore` se monta en `/var/lib/odoo` dentro del contenedor Odoo.
2. El parámetro `ir_attachment.location` no se sobreescribe en este proyecto, así que
   por defecto es `file` (lo leí en `ir_attachment.py:59-60`).
3. Por tanto, los binarios se guardan en el **volumen Docker `filestore`**, no en el
   repositorio ni en la BD (por defecto).

Esto es lo que el usuario necesita entender. Voy a responder claramente, distinguiendo
entre metadatos (BD) y binario (volumen Docker), y aclarando que NO se guarda en el
repositorio de git.

Perfecto, ahora tengo la confirmación completa de cómo está configurado este proyecto.
Respondo:

---

# Respuesta corta

**No, no se guardan en el repositorio.** En este proyecto (Doodba con la configuración
por defecto) los binarios se guardan en un **volumen Docker** llamado `filestore`,
montado en `/var/lib/odoo` dentro del contenedor Odoo. Lo que sí va a la **base de
datos** es la "ficha" del adjunto (metadatos) y, solo en ciertos casos, el contenido
binario.

---

# Detalle: qué va a la BD y qué va al disco

Odoo separa el adjunto en dos partes. La tabla `ir_attachment` de PostgreSQL guarda la
"ficha" (metadatos), y el contenido binario se guarda aparte según el parámetro
`ir_attachment.location`.

## 1. Lo que SIEMPRE va a la base de datos (PostgreSQL, tabla `ir_attachment`)

Los metadatos del fichero, independientemente del modo de almacenamiento:

| Columna                                                      | Contenido                                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------------- |
| `id`, `create_date`, `create_uid`, `write_date`, `write_uid` | Auditoría                                                           |
| `name`, `description`                                        | Nombre y descripción                                                |
| `res_model`, `res_id`, `res_field`, `res_name`               | A qué registro está vinculado                                       |
| `type`                                                       | `binary` o `url`                                                    |
| `url`                                                        | Si es de tipo URL                                                   |
| `mimetype`, `file_size`, `checksum` (SHA1)                   | Metadatos técnicos                                                  |
| `index_content`                                              | Texto indexable para buscar dentro del documento                    |
| `public`, `access_token`, `company_id`                       | Permisos / multi-compañía                                           |
| `store_fname`                                                | Si está en disco: la ruta relativa `XX/<sha1>` dentro del filestore |
| `db_datas`                                                   | Si está en BD: el contenido binario en `bytea`                      |

## 2. El contenido binario (los bytes del fichero) — depende de `ir_attachment.location`

El método `_storage()` en `ir_attachment.py:59-60` lee el parámetro de sistema
`ir_attachment.location`:

```python
return self.env['ir.config_parameter'].sudo().get_param('ir_attachment.location', 'file')
```

Es decir, **por defecto es `file`** y, como en este proyecto no se ha sobreescrito ese
parámetro en `conf.d/`, los binarios van al **filestore en disco**, no a la BD.

### Modo `file` (el que aplica aquí)

- Los bytes se escriben en `filestore/<dbname>/<XX>/<sha1>` donde `XX` son los dos
  primeros caracteres del SHA1 (se dispersa en 256 subdirectorios para no llenar un
  único dir).
- Deduplica por contenido: dos adjuntos idénticos ocupan un solo fichero físico.
- En la columna `store_fname` queda la ruta relativa (`XX/<sha1>`); en `db_datas` queda
  a `NULL`.
- El garbage collector (`_file_gc`) borra ficheros huérfanos cuando se eliminan
  adjuntos.

### Modo `db` (alternativo, no activado aquí)

- Los bytes van a la columna `db_datas` (`bytea`) de la propia tabla `ir_attachment`.
- Útil para despliegues sin almacenamiento persistente o para simplificar backups, pero
  hace crecer la BD.

Otros valores posibles (poco comunes): esquemas personalizados vía un módulo que
sobrescriba `_file_write`/`_file_read` (S3, etc.).

---

# Dónde vive físicamente el filestore en ESTE proyecto

Lo define `common.yaml:17` (compartido por `devel.yaml`, `test.yaml`, `prod.yaml`):

```yaml
volumes:
  - filestore:/var/lib/odoo
```

Y `devel.yaml:153-155` declara el volumen:

```yaml
volumes:
  filestore:
  db:
```

Por tanto:

- **Dentro del contenedor Odoo**: `/var/lib/odoo/filestore/<dbname>/` (en dev,
  `dbname=devel`).
- **En el host**: es un **volumen Docker nombrado** `tutorial_filestore` (no un bind
  mount), gestionado por Docker en `/var/lib/docker/volumes/...`. No es un directorio
  del repositorio.
- **No se versiona en git**: el `.gitignore` del scaffold excluye `odoo/auto/` y otros
  generados, pero el filestore ni siquiera vive dentro del árbol del repo — está en el
  volumen Docker.

Para inspeccionarlo en 运行时刻:

```bash
docker compose -f devel.yaml exec odoo ls -la /var/lib/odoo/filestore/devel/
docker volume inspect tutorial_filestore
```

Los ficheros físicos tienen nombres como `ab/ab12cd34...` (SHA1), sin extensión. No son
legibles directamente; para descargarlos se usa el ORM o el chatter.

---

# Lo que NO es el repositorio

Importante: aunque el código de tus módulos privados (`odoo/custom/src/private/`) está
montado en el contenedor, los adjuntos **nunca** se guardan ahí. El filestore es un
volumen independiente, montado en `/var/lib/odoo`, separado tanto del código fuente
(read-only en `/opt/odoo/custom`) como del repositorio git. Si borraras el repo, los
adjuntos seguirían existiendo en el volumen Docker (hasta que lo purgues con
`docker volume rm` o `invoke stop --purge`).

---

# Implicaciones operativas

1. **Backup**: hay que respaldar la BD **y** el volumen `filestore`. Si solo backupeas
   la BD pierdes los binarios; si solo backupeas el volumen pierdes los metadatos (y los
   ficheros quedan huérfanos sin saber a qué registros pertenecen).
2. **Restaurar en otro entorno**: hay que restaurar ambos (BD + filestore). Por eso
   `tasks.py` tiene snapshots combinados (líneas 1280 y 1313: "Snapshot current database
   and filestore" / "Restore database and filestore snapshot").
3. **Migrar a `db` storage** (si quisieras): en Ajustes → Técnico → Parámetros del
   sistema, crear/editar `ir_attachment.location = db` y luego ejecutar
   `ir.attachment.force_storage()` (método en `ir_attachment.py:74`) para migrar los
   existentes. El sentido inverso (de `db` a `file`) funciona igual. No es algo que
   necesites ahora; lo menciono para completitud.
4. **Tamaño**: los metadatos en la BD ocupan poco; el volumen crece con los binarios.
   Para imágenes, Odoo redimensiona automáticamente a máximo 1920x1920 por defecto
   (`_postprocess_contents`, `ir_attachment.py:328-369`) para no inflar el filestore.

---

# Resumen de un vistazo

| Parte                               | Dónde                                                                                             | Cómo se llama         |
| ----------------------------------- | ------------------------------------------------------------------------------------------------- | --------------------- |
| Metadatos del adjunto               | PostgreSQL                                                                                        | Tabla `ir_attachment` |
| Binario (modo por defecto `file`)   | Volumen Docker `filestore` → `/var/lib/odoo/filestore/<dbname>/<XX>/<sha1>` dentro del contenedor | filestore             |
| Binario (modo `db`, no activo aquí) | PostgreSQL, columna `db_datas`                                                                    | bytea                 |
| Código del repo                     | Sistema de ficheros del host                                                                      | NO guarda adjuntos    |

No he modificado nada, solo verificado la configuración.

---
